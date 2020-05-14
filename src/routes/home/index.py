from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file
from src.routes.warps.wraps import loginRequired
from src import mysql, bcrypt
from fpdf import FPDF
import datetime
import gc

indexRoutes = Blueprint('index', __name__, )


@indexRoutes.route('/home')
@indexRoutes.route('/')
def home():
    return render_template('home/Home.html')


@indexRoutes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('home/signup.html')

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if name == '' or email == '' or password == '':
            flash(u'Empty fields are not allowed', 'Error')
            return redirect(url_for("index.signup"))

        try:
            email.index('@')
            email.index('.')
        except:
            flash(u'invalid email', 'Error')
            return redirect(url_for("index.signup"))

        password = bcrypt.generate_password_hash(password)

        cursor = mysql.get_db().cursor()

        cursor.execute("INSERT INTO `com_nucleo_medico_user`(`name`, `email`, `password`) VALUES (%s, %s, %s)",
                       (name, email, password))

        mysql.get_db().commit()

        return redirect(url_for("index.signin"))


@indexRoutes.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "GET":
        return render_template('home/signin.html')

    if request.method == "POST":
        cursor = mysql.get_db().cursor()
        try:
            if session['id']:
                flash(u'You already have an active session', 'Error')
                return redirect(url_for("index.home"))
        except:
            pass

        if request.form['email']:
            cursor.execute(
                "SELECT * FROM `com_nucleo_medico_user` WHERE `com_nucleo_medico_user`.`email` LIKE %s", (request.form['email']))

            user = cursor.fetchone()

            if user:
                if bcrypt.check_password_hash(user[3], request.form['password']):
                    session['id'] = user[0]
                    session['name'] = user[1]
                    session['isDoctor'] = True
                    return redirect(url_for("root.nucleo"))

                flash(u'User or password error', 'Error')
                return redirect(url_for("index.signin"))

            else:
                cursor.execute(
                    "SELECT `id`, `nombre`, `password`, `change_password`, `id_own` FROM `com_nucleo_medico_empleados` WHERE `com_nucleo_medico_empleados`.`correo` LIKE %s", (request.form['email']))

                empleado = cursor.fetchone()

                if empleado:
                    if bcrypt.check_password_hash(empleado[2], request.form['password']):
                        session['id'] = empleado[0]
                        session['name'] = empleado[1]
                        session['id_own'] = empleado[4]
                        session['isDoctor'] = False
                        if empleado[3] == 1:
                            return redirect(url_for("index.changePassword"))
                        return redirect(url_for("index.home"))

                flash(u'User or password error', 'Error')
                return redirect(url_for("index.signin"))
        else:
            flash(u'Empty fields are not allowed', 'Error')
            return redirect(url_for("index.signin"))


@indexRoutes.route('/changePassword', methods=['GET', 'POST'])
@loginRequired
def changePassword():

    if request.method == "GET":
        return render_template('home/changePassword.html')

    password = request.form['password']
    confirmPassword = request.form['confirmPassword']

    if password == '' or confirmPassword == '':
        flash("Empty fields are not alloweds", 'Error')
        return redirect(url_for("index.changePassword"))

    if confirmPassword != password:
        flash("Passwords don't match", 'Error')
        return redirect(url_for("index.changePassword"))

    password = bcrypt.generate_password_hash(password)

    cursor = mysql.get_db().cursor()

    cursor.execute(
        "UPDATE `com_nucleo_medico_empleados` SET `password`=%s,`change_password`=0 WHERE `id`=%s", (password, session['id']))

    mysql.get_db().commit()

    return redirect(url_for("index.home"))


@indexRoutes.route('/signout')
@loginRequired
def signout():
    session.clear()
    gc.collect()
    return redirect(url_for("index.home"))


@indexRoutes.route('/about')
def about():
    return render_template('home/about.html')


@indexRoutes.route('/pdfMedicamentos')
@loginRequired
def pdfMedicamentos():

    cursor = mysql.get_db().cursor()
    cursor.execute('''
    SELECT `com_nucleo_medico_medicamentos`.`name`, `com_nucleo_medico_laboratorios`.`name` AS laboratorio, `com_nucleo_medico_proveedores`.`name` AS proveedor, `com_nucleo_medico_medicamentos_stock`.`cantidad`, IF(`com_nucleo_medico_medicamentos`.`delete` = 0, 'Activo', 'Eliminado') AS estado
    FROM `com_nucleo_medico_medicamentos` 
    INNER JOIN `com_nucleo_medico_laboratorios`
    ON `com_nucleo_medico_medicamentos`.`laboratory` = `com_nucleo_medico_laboratorios`.`id`
    INNER JOIN `com_nucleo_medico_proveedores`
    ON `com_nucleo_medico_proveedores`.`id` = `com_nucleo_medico_medicamentos`.`provider`
    INNER JOIN `com_nucleo_medico_medicamentos_stock`
    ON `com_nucleo_medico_medicamentos_stock`.`id` = `com_nucleo_medico_medicamentos`.`id`
    WHERE `com_nucleo_medico_medicamentos`.`own` = % s''', (session['id']))

    medicamentos = cursor.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    pdf.cell(50, 10, 'Fecha: %s/%s/%s' % (datetime.datetime.now().day,
                                          datetime.datetime.now().month, datetime.datetime.now().year), 0, 0, 'C')
    pdf.cell(80, 10, 'Medicines Report', 0, 1, 'C')
    pdf.cell(100, 10, '', 0, 1, 'C')
    pdf.cell(100, 10, '', 0, 1, 'C')

    if len(medicamentos) > 1:
        pdf.cell(50, 10, 'Name', 1, 0, 'C')
        pdf.cell(40, 10, 'Laboratorio', 1, 0, 'C')
        pdf.cell(40, 10, 'Proveedor', 1, 0, 'C')
        pdf.cell(20, 10, 'Stock', 1, 0, 'C')
        pdf.cell(30, 10, 'Status', 1, 1, 'C')
        for medicameto in medicamentos:
            name = medicameto[0]
            laboratorio = medicameto[1]
            proveedor = medicameto[2]

            if len(name) > 13:
                name = name[:11] + '...'
            if len(laboratorio) > 11:
                laboratorio = laboratorio[:9] + '...'
            if len(proveedor) > 11:
                proveedor = proveedor[:9] + '...'

            pdf.cell(50, 10, name, 1, 0, 'C')
            pdf.cell(40, 10, laboratorio, 1, 0, 'C')
            pdf.cell(40, 10, proveedor, 1, 0, 'C')
            pdf.cell(20, 10, str(medicameto[3]), 1, 0, 'C')
            pdf.cell(30, 10, medicameto[4], 1, 1, 'C')
    else:
        pdf.cell(80, 10, 'No hay datos para mostrar', 0, 0, 'C')

    pdf.output('src/data/reports/medicamentos.pdf', 'F')

    return send_file('data/reports/tuto1.pdf')
