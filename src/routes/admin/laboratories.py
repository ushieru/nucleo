from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired, onlyPOST
from src import mysql

laboratoriesRoutes = Blueprint('laboratories', __name__)


@laboratoriesRoutes.route('/laboratories')
@loginRequired
def laboratories():
    cursor = mysql.get_db().cursor()

    cursor.execute("""SELECT `com_nucleo_medico_laboratorios`.`id`, `com_nucleo_medico_laboratorios`.`name`, `com_nucleo_medico_laboratorios`.`email`, `com_nucleo_medico_laboratorios`.`address`, `com_nucleo_medico_laboratorios`.`telephone`, `com_nucleo_medico_laboratorios`.`isDelete`
                    FROM `com_nucleo_medico_laboratorios` 
                    INNER JOIN  `com_nucleo_medico_user`
                    ON `com_nucleo_medico_laboratorios`.`own` LIKE `com_nucleo_medico_user`.`id`
                    WHERE `com_nucleo_medico_user`.`id` LIKE %s""", (session['id']))

    labs = cursor.fetchall()

    return render_template('app/modules/admin/laboratories.html', labs=labs)


@laboratoriesRoutes.route('/laboratories/add', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def laboratoriesAdd():
    cursor = mysql.get_db().cursor()

    cursor.execute("""INSERT INTO `com_nucleo_medico_laboratorios` (`own`, `name`, `email`, `address`, `telephone`, `isDelete`) 
                    VALUES (%s, %s,  %s,  %s,  %s, 0)""",
                   (session['id'], request.form['name'], request.form['email'], request.form['address'], request.form['phone']))

    mysql.get_db().commit()

    return redirect(url_for("laboratories.laboratories"))


@laboratoriesRoutes.route('/laboratories/edit', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def laboratoriesEdit():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_laboratorios` SET `name`=%s,`email`=%s,`address`=%s,`telephone`=%s 
                    WHERE `id` = %s""",
                   (request.form['name'], request.form['email'], request.form['address'], request.form['phone'], request.form['id']))

    mysql.get_db().commit()

    return redirect(url_for("laboratories.laboratories"))


@laboratoriesRoutes.route('/laboratories/delete', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def laboratoriesDelete():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_laboratorios` 
                    SET  `isDelete`= 1 
                    WHERE `id` LIKE %s""",
                   (request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for("laboratories.laboratories"))


@laboratoriesRoutes.route('/laboratories/restore', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def laboratoriesRestore():
    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_laboratorios` 
                    SET  `isDelete`= 0 
                    WHERE `id` LIKE %s""",
                   (request.form['value']))

    mysql.get_db().commit()

    return redirect(url_for("laboratories.laboratories"))
