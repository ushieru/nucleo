from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired, onlyPOST
from src import mysql

providersRoutes = Blueprint('providers', __name__)


@providersRoutes.route('/providers')
@loginRequired
def providers():
    cursor = mysql.get_db().cursor()

    cursor.execute("""SELECT `com_nucleo_medico_proveedores`.`id`, `com_nucleo_medico_proveedores`.`name`, `com_nucleo_medico_proveedores`.`email`, `com_nucleo_medico_proveedores`.`address`, `com_nucleo_medico_proveedores`.`telephone`, `com_nucleo_medico_proveedores`.`isDelete`
                    FROM `com_nucleo_medico_proveedores` 
                    INNER JOIN  `com_nucleo_medico_user`
                    ON `com_nucleo_medico_proveedores`.`own` LIKE `com_nucleo_medico_user`.`id`
                    WHERE `com_nucleo_medico_user`.`id` LIKE %s""", (session['id']))

    provs = cursor.fetchall()

    return render_template('app/modules/admin/providers.html', provs=provs)


@providersRoutes.route('/providers/add', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def providersAdd():
    cursor = mysql.get_db().cursor()

    cursor.execute("""INSERT INTO `com_nucleo_medico_proveedores`(`own`, `name`, `email`, `address`, `telephone`, `isDelete`)
                    VALUES (%s, %s,  %s,  %s,  %s, 0)""",
                   (session['id'], request.form['name'], request.form['email'], request.form['address'], request.form['phone']))

    mysql.get_db().commit()

    return redirect(url_for("providers.providers"))


@providersRoutes.route('/providers/edit', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def providersEdit():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_proveedores` SET `name`=%s,`email`=%s,`address`=%s,`telephone`=%s 
                    WHERE `id` = %s""",
                   (request.form['name'], request.form['email'], request.form['address'], request.form['phone'], request.form['id']))

    mysql.get_db().commit()
    return redirect(url_for("providers.providers"))


@providersRoutes.route('/providers/delete', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def providersDelete():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_proveedores` 
                    SET  `isDelete`= 1 
                    WHERE `id` LIKE %s""",
                   (request.form['value']))

    mysql.get_db().commit()
    return redirect(url_for("providers.providers"))


@providersRoutes.route('/providers/restore', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def providersRestore():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_proveedores` 
                    SET  `isDelete`= 0
                    WHERE `id` LIKE %s""",
                   (request.form['value']))

    mysql.get_db().commit()
    return redirect(url_for("providers.providers"))
