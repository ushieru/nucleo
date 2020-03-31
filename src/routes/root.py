from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired

rootRoutes = Blueprint('root', __name__)


@rootRoutes.route('/admin')
@loginRequired
def admin():
    return render_template('app/admin.html')

@rootRoutes.route('/hospital')
@loginRequired
def hospital():
    return render_template('app/hospital.html')

@rootRoutes.route('/settings')
@loginRequired
def settings():
    return render_template('app/settings.html')


@rootRoutes.route('/nucleo')
@loginRequired
def nucleo():
    userName = session["name"][:session["name"].find(" ")]
    return render_template('app/dashboard.html', userName=userName, numAppointments=0, numMedicines=0)
