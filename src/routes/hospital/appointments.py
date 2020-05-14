from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from src.routes.warps.wraps import loginRequired
from src import mysql

import datetime

appointmentsRoutes = Blueprint('appointments', __name__)


@appointmentsRoutes.route('/appointments', methods=['GET', 'POST'])
@loginRequired
def appointments():
    cursor = mysql.get_db().cursor()

    try:
        date = request.form['date']
    except:
        date = datetime.datetime.today()
        date = date.strftime('%Y-%m-%d')

    cursor.execute("""
        SELECT `com_nucleo_medico_citas`.`id`, `com_nucleo_medico_citas`.`own`, `com_nucleo_medico_pacientes`.`name`, `com_nucleo_medico_citas`.`hora`, `com_nucleo_medico_citas`.`descripcion`, `com_nucleo_medico_citas`.`status`
        FROM `com_nucleo_medico_citas` 
        INNER JOIN `com_nucleo_medico_pacientes` 
        ON `com_nucleo_medico_citas`.`paciente` = `com_nucleo_medico_pacientes`.`id` 
        WHERE `com_nucleo_medico_citas`.`fecha` = %s AND `com_nucleo_medico_citas`.`status` = 0 AND `com_nucleo_medico_citas`.`own` = %s
        """, (date, session['id']))

    appointments = cursor.fetchall()

    cursor.execute("""
        SELECT `com_nucleo_medico_pacientes`.`id`, `com_nucleo_medico_pacientes`.`name`
        FROM `com_nucleo_medico_pacientes`
        WHERE `com_nucleo_medico_pacientes`.`delete` = 0
        """)

    patients = cursor.fetchall()

    return render_template('app/modules/hospital/appointments.html', appointments=appointments, date=date, patients=patients)


@appointmentsRoutes.route('/appointments/add', methods=['POST'])
@loginRequired
def appointmentsAdd():

    if datetime.date(int(request.form['date'].split('-')[0]), int(request.form['date'].split('-')[1]), int(request.form['date'].split('-')[2])) < datetime.date.today():
        flash("You can't schedule an appointment with a date before today", 'Error')
        return redirect(url_for("appointments.appointments"))

    if datetime.datetime.now().hour > int(request.form['hour'][:2]):
        flash("You can't make an appointment with an hour past", 'Error')
        return redirect(url_for("appointments.appointments"))

    if datetime.datetime.now().minute > int(request.form['hour'][3:5]):
        flash("You can't make an appointment with an hour past", 'Error')
        return redirect(url_for("appointments.appointments"))

    cursor = mysql.get_db().cursor()

    cursor.execute("""SELECT `hora` FROM `com_nucleo_medico_citas` WHERE `fecha` = %s AND `own` = %s AND `status` = 0
    """, (request.form['date'], session['id']))

    if str(cursor.fetchone()[0])[:3] == request.form['hour'][:3]:
        flash("You can't register an appointment with an already scheduled time", 'Error')
        return redirect(url_for("appointments.appointments"))

    cursor.execute("""
        INSERT INTO `com_nucleo_medico_citas`(`own`, `paciente`, `fecha`, `hora`, `descripcion`) 
        VALUES (%s, %s, %s, %s, %s)
        """, (session['id'], request.form['patient'], request.form['date'], request.form['hour'], request.form['description']))

    mysql.get_db().commit()

    return redirect(url_for('appointments.appointments'))


@appointmentsRoutes.route('/appointments/check', methods=['POST'])
@loginRequired
def appointmentsCheck():
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        UPDATE `com_nucleo_medico_citas` 
        SET `status`= 1 
        WHERE `id`=  %s
        """, (request.form['id']))

    mysql.get_db().commit()

    return redirect(url_for('appointments.appointments'))


@appointmentsRoutes.route('/appointments/cancel', methods=['POST'])
@loginRequired
def appointmentsCancel():
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        UPDATE `com_nucleo_medico_citas` 
        SET `status`= 2 
        WHERE `id`=  %s
        """, (request.form['id']))

    mysql.get_db().commit()

    return redirect(url_for('appointments.appointments'))
