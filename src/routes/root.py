from flask import Blueprint, render_template, request, redirect, url_for

rootRoutes = Blueprint('root', __name__)


@rootRoutes.route('/admin')
def admin():
    return render_template('app/admin.html')

@rootRoutes.route('/hospital')
def hospital():
    return render_template('app/hospital.html')

@rootRoutes.route('/settings')
def settings():
    return render_template('app/settings.html')


@rootRoutes.route('/nucleo')
def nucleo():
    return render_template('app/dashboard.html', userName="Ushieru", numAppointments=0, numMedicines=0)
