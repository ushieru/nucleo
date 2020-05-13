from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

prescriptionsRoutes = Blueprint('prescriptions', __name__)


@prescriptionsRoutes.route('/prescriptions', methods=['GET', 'POST'])
@loginRequired
def prescriptions():
    if request.method == "POST":
        cursor = mysql.get_db().cursor()

        cursor.execute("""
            UPDATE `com_nucleo_medico_citas` 
            SET `status`= 1 
            WHERE `id`=  %s
            """, (request.form['id']))

        mysql.get_db().commit()

        cursor.execute("""
            SELECT `com_nucleo_medico_pacientes`.`name`, `com_nucleo_medico_pacientes`.`id` 
            FROM `com_nucleo_medico_citas` 
            INNER JOIN `com_nucleo_medico_pacientes`
            ON `com_nucleo_medico_citas`.`paciente` = `com_nucleo_medico_pacientes`.`id`
            WHERE `com_nucleo_medico_citas`.`id` = %s
            """, (request.form['id']))

        userName = cursor.fetchone()

        return render_template('app/modules/hospital/prescriptions.html', id=userName[1], userName=userName)

    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT `com_nucleo_medico_pacientes`.`id`, `com_nucleo_medico_pacientes`.`name`, `com_nucleo_medico_pacientes`.`email`
        FROM `com_nucleo_medico_pacientes` WHERE `com_nucleo_medico_pacientes`.`own` = %s AND `com_nucleo_medico_pacientes`.`delete` = 0
        """, (session['id']))

    users = cursor.fetchall()

    return render_template('app/modules/hospital/files.html', users=users, prescription=True)


@prescriptionsRoutes.route('/prescriptionsAdd', methods=['GET', 'POST'])
@loginRequired
def prescriptionsAdd():
    if request.method == "POST":
        cursor = mysql.get_db().cursor()

        cursor.execute("""
            INSERT INTO `com_nucleo_medico_recetas`(`id_own`, `id_paciente`, `prescripcion`) 
            VALUES (%s, %s, %s)
            """, (session['id'], request.form['id'], request.form['prescription']))

        mysql.get_db().commit()

        cursor.execute("""
            INSERT INTO `com_nucleo_medico_highlights`(`id_paciente`, `highlight`) 
            VALUES (%s, %s)
            """, (request.form['id'], request.form['highlight']))

        mysql.get_db().commit()

    return redirect(url_for('appointments.appointments'))
