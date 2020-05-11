from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired, onlyPOST
from src import mysql, bcrypt

import random
import string

employeesRoutes = Blueprint('employees', __name__)


@employeesRoutes.route('/employees')
@loginRequired
def employees():

    return render_template('app/modules/admin/employees.html')


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
