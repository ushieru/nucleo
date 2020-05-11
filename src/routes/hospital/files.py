from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

filesRoutes = Blueprint('files', __name__)


@filesRoutes.route('/files', methods=['GET','POST'])
@loginRequired
def files():
    cursor = mysql.get_db().cursor()
    
    cursor.execute("""
        SELECT `com_nucleo_medico_pacientes`.`id`, `com_nucleo_medico_pacientes`.`name`, `com_nucleo_medico_pacientes`.`email`
        FROM `com_nucleo_medico_pacientes` WHERE `com_nucleo_medico_pacientes`.`own` = %s AND `com_nucleo_medico_pacientes`.`delete` = 0
        """, (session['id']))

    users = cursor.fetchall()
    return render_template('app/modules/hospital/files.html', users=users)

@filesRoutes.route('/filesView', methods=['GET','POST'])
@loginRequired
def filesView():
    cursor = mysql.get_db().cursor()
    
    cursor.execute("""
        SELECT `prescripcion`, `fecha`
        FROM `com_nucleo_medico_recetas` 
        WHERE `com_nucleo_medico_recetas`.`id_paciente` = %s 
        ORDER BY `com_nucleo_medico_recetas`.`fecha` DESC
        """, (request.form['userID']))

    files = cursor.fetchall()

    cursor.execute("""
        SELECT `com_nucleo_medico_pacientes`.`name`
        FROM `com_nucleo_medico_recetas` 
        INNER JOIN `com_nucleo_medico_pacientes`
        ON `com_nucleo_medico_pacientes`.`id` = `com_nucleo_medico_recetas`.`id_paciente`
        WHERE `com_nucleo_medico_recetas`.`id_paciente` = %s
        LIMIT 1
        """, (request.form['userID']))

    userName = cursor.fetchone()

    cursor.execute("""
        SELECT `highlight` 
        FROM `com_nucleo_medico_highlights` 
        WHERE `id_paciente` =  %s
        """, (request.form['userID']))

    highlights = cursor.fetchall()

    return render_template('app/modules/hospital/filesView.html', files=files, userName=userName[0], highlights=highlights)
    