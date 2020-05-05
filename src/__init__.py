from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# CONFIGURATION
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "nucleo"
app.config['SECRET_KEY'] = "NucleoSecretKey"

# MIDDLEWARES
mysql = MySQL()
mysql.init_app(app)
bcrypt = Bcrypt(app)

# ROOT ROUTES
@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404


# ROUTES IMPORT
from src.routes.admin.reports import reportsRoutes
from src.routes.admin.patients import patientsRoutes
from src.routes.admin.medicines import medicinesRoutes
from src.routes.admin.providers import providersRoutes
from src.routes.admin.laboratories import laboratoriesRoutes
from src.routes.hospital.appointments import appointmentsRoutes
from src.routes.root import rootRoutes
from src.routes.home.index import indexRoutes

# REGISTER BLUEPRINTS
app.register_blueprint(indexRoutes)
app.register_blueprint(rootRoutes)
app.register_blueprint(laboratoriesRoutes, url_prefix="/admin")
app.register_blueprint(providersRoutes, url_prefix="/admin")
app.register_blueprint(medicinesRoutes, url_prefix="/admin")
app.register_blueprint(patientsRoutes, url_prefix="/admin")
app.register_blueprint(reportsRoutes, url_prefix="/admin")
app.register_blueprint(appointmentsRoutes, url_prefix="/hospital")
