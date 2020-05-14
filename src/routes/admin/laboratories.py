from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from src.routes.warps.wraps import loginRequired, onlyPOST
from src import mysql

laboratoriesRoutes = Blueprint('laboratories', __name__)


@laboratoriesRoutes.route('/laboratories')
@loginRequired
def laboratories():
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT `com_nucleo_medico_laboratorios`.`id`, `com_nucleo_medico_laboratorios`.`name`, `com_nucleo_medico_laboratorios`.`email`, `com_nucleo_medico_laboratorios`.`address`, `com_nucleo_medico_laboratorios`.`telephone`, `com_nucleo_medico_laboratorios`.`isDelete`
        FROM `com_nucleo_medico_laboratorios` 
        INNER JOIN  `com_nucleo_medico_user`
        ON `com_nucleo_medico_laboratorios`.`own` LIKE `com_nucleo_medico_user`.`id`
        WHERE `com_nucleo_medico_user`.`id` LIKE %s
        """, (session['id']))

    labs = cursor.fetchall()

    return render_template('app/modules/admin/laboratories.html', labs=labs)


@laboratoriesRoutes.route('/laboratories/add', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def laboratoriesAdd():

    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phone']

    if name == '' or email == '' or address == '' or phone == '':
        flash(u'Empty fields are not allowed', 'Error')
        return redirect(url_for("laboratories.laboratories"))

    try: 
        email.index('@')
        email.index('.')
    except:
        flash(u'Invalid email', 'Error')
        return redirect(url_for("laboratories.laboratories"))

    cursor = mysql.get_db().cursor()

    cursor.execute("""
        INSERT INTO `com_nucleo_medico_laboratorios` (`own`, `name`, `email`, `address`, `telephone`) 
        VALUES (%s, %s,  %s,  %s,  %s)
        """, (session['id'], name, email, address, phone))

    mysql.get_db().commit()

    return redirect(url_for("laboratories.laboratories"))


@laboratoriesRoutes.route('/laboratories/edit', methods=['GET', 'POST'])
@onlyPOST
@loginRequired
def laboratoriesEdit():

    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phone']
    id = request.form['id']

    if name == '' or email == '' or address == '' or phone == '' or id == '':
        flash(u'Empty fields are not allowed', 'Error')
        return redirect(url_for("laboratories.laboratories"))
    
    try: 
        email.index('@')
        email.index('.')
    except:
        flash(u'invalid email', 'Error')
        return redirect(url_for("laboratories.laboratories"))

    cursor = mysql.get_db().cursor()

    cursor.execute("""UPDATE `com_nucleo_medico_laboratorios` SET `name`=%s,`email`=%s,`address`=%s,`telephone`=%s 
                    WHERE `id` = %s""",
                   (name, email, address, phone, id))

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
