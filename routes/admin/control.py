from flask import Blueprint, render_template, request, redirect, url_for

controlRoutes = Blueprint('control', __name__)

@controlRoutes.route('/home')
@controlRoutes.route('/')
def home():
    return render_template('home/Home.html')

@controlRoutes.route('/signup')
def signup():
    return render_template('home/signup.html')

@controlRoutes.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "GET":
        return render_template('home/signin.html')

    if request.method == "POST":
        return redirect(url_for("control.nucleo"))

@controlRoutes.route('/signout')
def signout():
    return redirect(url_for("control.home"))

@controlRoutes.route('/nucleo')
def nucleo():
    return render_template('app/dashboard.html', userName="Ushieru", numAppointments=0, numMedicines=0)