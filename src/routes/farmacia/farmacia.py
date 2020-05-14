from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

farmaciaRoutes = Blueprint('farmacia', __name__)


@farmaciaRoutes.route('/', methods=['GET', 'POST'])
@loginRequired
def farmacia():
    
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT `com_nucleo_medico_medicamentos`.`id`, `com_nucleo_medico_medicamentos`.`name`, `com_nucleo_medico_laboratorios`.`name`, `com_nucleo_medico_medicamentos_stock`.`cantidad`
        FROM `com_nucleo_medico_medicamentos` 
        INNER JOIN `com_nucleo_medico_medicamentos_stock`
        ON `com_nucleo_medico_medicamentos`.`id` = `com_nucleo_medico_medicamentos_stock`.`id`
        INNER JOIN `com_nucleo_medico_laboratorios`
        ON `com_nucleo_medico_laboratorios`.`id` = `com_nucleo_medico_medicamentos`.`laboratory`
        WHERE `com_nucleo_medico_medicamentos`.`delete` = 0 AND `com_nucleo_medico_medicamentos`.`expiration` > CURRENT_DATE AND `com_nucleo_medico_medicamentos`.`own` = %s
        """, (session['id_own']))

    medicines = cursor.fetchall()

    return render_template('app/farmacia/farmacia.html', medicines=medicines)

@farmaciaRoutes.route('/addToStock', methods=['GET', 'POST'])
@loginRequired
def addToStock():

    if request.method == 'GET':
        return redirect(url_for('farmacia.farmacia'))
    
    idMedicine = request.form['idMedicine']
    quantity = request.form['quantity']

    cursor = mysql.get_db().cursor()

    print("UPDATE `com_nucleo_medico_medicamentos_stock` SET `cantidad`=%s WHERE `id`=%s" % (quantity, idMedicine))

    cursor.execute(
        "UPDATE `com_nucleo_medico_medicamentos_stock` SET `cantidad`=%s WHERE `id`=%s", (quantity, idMedicine))

    mysql.get_db().commit()

    return redirect(url_for('farmacia.farmacia'))