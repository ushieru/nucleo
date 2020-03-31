from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired, onlyPOST
from src import mysql

medicinesRoutes = Blueprint('medicines', __name__)


@medicinesRoutes.route('/medicines')
@loginRequired
def medicines():
    cursor = mysql.get_db().cursor()

    cursor.execute("""SELECT `com_nucleo_medico_proveedores`.`id`, `com_nucleo_medico_proveedores`.`name`
                    FROM `com_nucleo_medico_proveedores` 
                    INNER JOIN  `com_nucleo_medico_user`
                    ON `com_nucleo_medico_proveedores`.`own` LIKE `com_nucleo_medico_user`.`id`
                    WHERE `com_nucleo_medico_user`.`id` LIKE %s AND `com_nucleo_medico_proveedores`.`isDelete` LIKE 0""", (session['id']))

    provs = cursor.fetchall()

    cursor.execute("""SELECT `com_nucleo_medico_laboratorios`.`id`, `com_nucleo_medico_laboratorios`.`name`
                    FROM `com_nucleo_medico_laboratorios` 
                    INNER JOIN  `com_nucleo_medico_user`
                    ON `com_nucleo_medico_laboratorios`.`own` LIKE `com_nucleo_medico_user`.`id`
                    WHERE `com_nucleo_medico_user`.`id` LIKE %s AND `com_nucleo_medico_laboratorios`.`isDelete` LIKE 0""", (session['id']))

    labs = cursor.fetchall()

    cursor.execute("""SELECT `com_nucleo_medico_medicamentos`.`id`, `com_nucleo_medico_medicamentos`.`name`, `com_nucleo_medico_medicamentos`.`expiration`, `com_nucleo_medico_laboratorios`.`name`, `com_nucleo_medico_proveedores`.`name`, `com_nucleo_medico_medicamentos`.`delete` 
                    FROM `com_nucleo_medico_medicamentos` 
                    INNER JOIN `com_nucleo_medico_laboratorios`
                    ON `com_nucleo_medico_laboratorios`.`id` LIKE `com_nucleo_medico_medicamentos`.`laboratory`
                    INNER JOIN `com_nucleo_medico_proveedores`
                    ON `com_nucleo_medico_proveedores`.`id` LIKE `com_nucleo_medico_medicamentos`.`provider`
                    WHERE `com_nucleo_medico_medicamentos`.`own` 
                    LIKE %s ORDER BY `com_nucleo_medico_medicamentos`.`name` ASC""", (session['id']))

    meds = cursor.fetchall()

    return render_template('app/modules/admin/medicines.html', meds=meds, labs=labs, provs=provs)


@medicinesRoutes.route('/medicines/add', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def medicinesAdd():
    cursor = mysql.get_db().cursor()

    cursor.execute("""INSERT INTO `com_nucleo_medico_medicamentos`(`own`, `name`, `expiration`, `laboratory`, `provider`, `delete`) VALUES (%s, %s, %s, %s, %s, 0)""",
                   (session['id'], request.form['name'], request.form['expiration'], request.form['laboratories'], request.form['providers']))

    mysql.get_db().commit()

    return redirect(url_for("medicines.medicines"))


@medicinesRoutes.route('/medicines/edit', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def medicinesEdit():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_medicamentos` SET `name`=%s,`expiration`=%s,`laboratory`=%s,`provider`=%s WHERE `id` LIKE %s""",
                   (request.form['name'], request.form['expiration'], request.form['laboratories'], request.form['providers'], request.form['id']))

    mysql.get_db().commit()

    return redirect(url_for("medicines.medicines"))


@medicinesRoutes.route('/medicines/delete', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def medicinesDelete():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_medicamentos` 
                    SET  `delete`= 1
                    WHERE `id` LIKE %s""",
                   (request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for("medicines.medicines"))


@medicinesRoutes.route('/medicines/restore', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def medicinesRestore():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_medicamentos` 
                    SET  `delete`= 0
                    WHERE `id` LIKE %s""",
                   (request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for("medicines.medicines"))
