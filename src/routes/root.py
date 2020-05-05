from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

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
