from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404

# ADMIN
@app.route('/admin')
def admin():
    return render_template('app/admin.html')

## ROUTES IMPORT
from routes.admin.control import controlRoutes
from routes.admin.laboratories import laboratoriesRoutes
from routes.admin.providers import providersRoutes
from routes.admin.medicines import medicinesRoutes
from routes.admin.patients import patientsRoutes
from routes.admin.reports import reportsRoutes

## REGISTER BLUEPRINTS
app.register_blueprint(controlRoutes)
app.register_blueprint(laboratoriesRoutes, url_prefix="/admin")
app.register_blueprint(providersRoutes, url_prefix="/admin")
app.register_blueprint(medicinesRoutes, url_prefix="/admin")
app.register_blueprint(patientsRoutes, url_prefix="/admin")
app.register_blueprint(reportsRoutes, url_prefix="/admin")

# HOSPITAL
@app.route('/hospital')
def hospital():
    return render_template('app/hospital.html')

# SETTINGS
@app.route('/settings')
def settings():
    return render_template('app/settings.html')


if __name__ == '__main__':
    # Add host='0.0.0.0' to set visible
    app.run(port=3000, debug=True)
