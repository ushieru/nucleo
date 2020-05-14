from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from src.routes.warps.wraps import loginRequired
from src import mysql, bcrypt
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