from flask import Blueprint, render_template, request, redirect, url_for, session
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

        cursor.execute(
            "SELECT * FROM `com_nucleo_medico_user` WHERE `com_nucleo_medico_user`.`email` LIKE %s", (request.form['email']))

        user = cursor.fetchone()

        print(user)

        if len(user) > 0:
            if bcrypt.check_password_hash(user[3], request.form['password']):
                session['id'] = user[0]
                session['name'] = user[1]

                return redirect(url_for("root.nucleo"))


@indexRoutes.route('/signout')
@loginRequired
def signout():
    session.clear()
    gc.collect()
    return redirect(url_for("index.home"))
