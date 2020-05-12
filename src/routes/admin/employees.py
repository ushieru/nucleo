from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired, onlyPOST
from src import mysql, bcrypt

import random
import string

employeesRoutes = Blueprint('employees', __name__)


@employeesRoutes.route('/employees')
@loginRequired
def employees():
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT `id`, `nombre`, `correo`, `telefono`, `status`
        FROM `com_nucleo_medico_empleados` 
        WHERE `id_own` = %s
        """, (session['id']))

    employees = cursor.fetchall()

    return render_template('app/modules/admin/employees.html', employees=employees)


@employeesRoutes.route('/employeeAdd', methods=['GET', 'POST'])
@loginRequired
def employeeAdd():

    cursor = mysql.get_db().cursor()

    passwordAux = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))

    password = bcrypt.generate_password_hash(passwordAux)

    cursor.execute("""
        INSERT INTO `com_nucleo_medico_empleados`(`id_own`, `nombre`, `correo`, `telefono`, `password`) 
        VALUES (%s, %s, %s, %s, %s)
        """, (session['id'], request.form['name'], request.form['email'], request.form['phone'], password))

    mysql.get_db().commit()

    return redirect(url_for('root.sendMail', name=request.form['name'], email=request.form['email'], password=passwordAux))


@employeesRoutes.route('/employeeEdit', methods=['GET', 'POST'])
@loginRequired
def employeeEdit():
    
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        UPDATE `com_nucleo_medico_empleados` 
        SET `nombre`=%s,`correo`=%s,`telefono`=%s 
        WHERE `id`=%s
        """, (request.form['name'], request.form['email'], request.form['phone'], request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for('employees.employees'))


@employeesRoutes.route('/employeeRestore', methods=['GET', 'POST'])
@loginRequired
def employeeRestore():

    cursor = mysql.get_db().cursor()

    cursor.execute("""
        UPDATE `com_nucleo_medico_empleados` SET `status`= 0 WHERE `id` = %s
        """, (request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for('employees.employees'))


@employeesRoutes.route('/employeeDelete', methods=['GET', 'POST'])
@loginRequired
def employeeDelete():

    cursor = mysql.get_db().cursor()

    cursor.execute("""
        UPDATE `com_nucleo_medico_empleados` SET `status`= 1 WHERE `id` = %s
        """, (request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for('employees.employees'))
