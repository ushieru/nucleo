from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql, mail, Message

import datetime

rootRoutes = Blueprint('root', __name__)


@rootRoutes.route('/admin')
@loginRequired
def admin():
    return render_template('app/admin.html')


@rootRoutes.route('/hospital')
@loginRequired
def hospital():
    return render_template('app/hospital.html')


@rootRoutes.route('/settings')
@loginRequired
def settings():
    return render_template('app/settings.html')


@rootRoutes.route('/nucleo')
@loginRequired
def nucleo():
    cursor = mysql.get_db().cursor()

    date = datetime.datetime.today()
    date = date.strftime('%Y-%m-%d')

    cursor.execute("""
        SELECT COUNT(`com_nucleo_medico_citas`.`id`) AS total
        FROM `com_nucleo_medico_citas` 
        INNER JOIN `com_nucleo_medico_pacientes` 
        ON `com_nucleo_medico_citas`.`paciente` = `com_nucleo_medico_pacientes`.`id` 
        WHERE `com_nucleo_medico_citas`.`fecha` = %s AND `com_nucleo_medico_citas`.`status` = 0 AND `com_nucleo_medico_citas`.`own` = %s
        """, (date, session['id']))

    numAppointments = cursor.fetchone()

    userName = session["name"][:session["name"].find(" ")]
    return render_template('app/dashboard.html', userName=userName, numAppointments=numAppointments[0], numMedicines=0)


@rootRoutes.route('/sendMail/<name>/<email>/<password>', methods=['GET', 'POST'])
@loginRequired
def sendMail(name, email, password):
    if email and password:
        msg = Message("Hello",
                      recipients=[email])

        msg.html = """
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr style="background-color: #2780E3;">
                <td>
                    <table>
                        <tr>
                            <td>
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Wiki_Project_Med_Foundation_logo.svg/800px-Wiki_Project_Med_Foundation_logo.svg.png"
                                    alt="VaraS de Esculapio" width="42" style="padding: 5px;">
                            </td>
                            <td style="vertical-align: middle; height: 42px;">
                                <span style="color:azure; padding: 5px;">Nucleo Medico</span>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td align="center" style="background-color: #eeeeee;">
                    <table border="0" cellpadding="0" cellspacing="0" width="80%" style="margin: 15px; background-color: white; padding: 10px 15px;">
                        <tr>
                            <td>
                                <p>Hola, """ + name + """:</p>
                            </td>
                        </tr>
                        <tr>
                            <td style="color: #757575; padding: 0 10px;">
                                <p>Se te a invitado a colaborar con el doctor $doctor, en su farmacia.</p>
                                <p>Tu usuario es tu correo electronico. Su contrase&ntilde;a sera provisional solo para su primer ingreso, no la comparta con nadie, en ningun momento.</p>
                                <p style="color: #01579b; padding-left: 15px;">""" + password + """</p>
                            </td>
                        </tr>
                        <tr>
                            <td style="color: #757575;">
                                <br>
                                <br>
                                <p style="font-size: x-small;">El contenido de este email es totalmente privado no se debe ser compartido con nadie en ningun momento.</p>
                            </td>
                    </table>
                </td>
            </tr>
        </table>
        """

        try:
            mail.send(msg)
        except Exception as identifier:
            return str(identifier)
            
    return redirect(url_for('employees.employees'))
