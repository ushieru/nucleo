from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

appointmentsRoutes = Blueprint('appointments', __name__, )


@appointmentsRoutes.route('/appointments')
@loginRequired
def appointments():
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT `com_nucleo_medico_citas`.`id`, `com_nucleo_medico_citas`.`own`, `com_nucleo_medico_pacientes`.`name`, `com_nucleo_medico_citas`.`hora`, `com_nucleo_medico_citas`.`descripcion`, `com_nucleo_medico_citas`.`delete`
        FROM `com_nucleo_medico_citas` 
        INNER JOIN `com_nucleo_medico_pacientes` 
        ON `com_nucleo_medico_citas`.`paciente` = `com_nucleo_medico_pacientes`.`id` 
        WHERE `com_nucleo_medico_citas`.`fecha` = CURRENT_DATE
        """)

    appointments = cursor.fetchall()

    return render_template('app/modules/hospital/appointments.html', appointments=appointments)