from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

patientsRoutes = Blueprint('patients', __name__)


@patientsRoutes.route('/patients')
@loginRequired
def patients():
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT `com_nucleo_medico_pacientes`.`id`, `com_nucleo_medico_pacientes`.`name`, `com_nucleo_medico_pacientes`.`email`, `com_nucleo_medico_pacientes`.`domicilio`, `com_nucleo_medico_pacientes`.`celular`, `com_nucleo_medico_pacientes`.`delete` 
        FROM `com_nucleo_medico_pacientes` WHERE `com_nucleo_medico_pacientes`.`own` = %s
        """, (session['id']))

    patients = cursor.fetchall()

    return render_template('app/modules/admin/patients.html', pats=patients)


@patientsRoutes.route('/patients/gestor', methods=['GET', 'POST'])
def patientsGestor():
    if request.method == "GET":
        return redirect(url_for("root.nucleo"))

    if request.method == "POST":
        if request.form.get("value") == "-1":
            return "Search %s" % (request.form.get("search"))

        if request.form.get("value") == "0":
            return render_template('app/modules/admin/patientsadd.html', title="Add Patient", pat=[])
        else:
            cursor = mysql.get_db().cursor()

            cursor.execute("""
                SELECT `id`, `name`, `birthday`, `sexo`, `email`, `ocupacion`, `escolaridad`, `curp`, `poliza`, `estado_civil`, `domicilio`, `colonia`, `estado`, `municipio`, `celular`, `tel_casa`, `tel_oficina`, `delete`
                FROM `com_nucleo_medico_pacientes` 
                WHERE  `com_nucleo_medico_pacientes`.`id` = %s
                """, (request.form.get("id")))

            patients = cursor.fetchone()
            return render_template('app/modules/admin/patientsadd.html', title="Edit Patient", pat=patients)


@patientsRoutes.route('/patients/add', methods=['GET', 'POST'])
@loginRequired
def patientsAdd():
    if request.method == "GET":
        return redirect(url_for("root.nucleo"))

    if request.method == "POST":
        cursor = mysql.get_db().cursor()

        cursor.execute("""
            INSERT INTO `com_nucleo_medico_pacientes`(`own`, `name`, `birthday`, `sexo`, `email`, `ocupacion`, `escolaridad`, `curp`, `poliza`, `estado_civil`, `domicilio`, `colonia`, `estado`, `municipio`, `celular`, `tel_casa`, `tel_oficina`) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (session['id'], request.form['name'], request.form['birthday'], request.form['gender'], request.form['email'], request.form['occupation'], request.form['scholarship'], request.form['id'], request.form['lin'], request.form['mStatus'], request.form['address'], request.form['suburb'], request.form['government'], request.form['city'], request.form['phone'], request.form['hPhone'], request.form['oPhone']))

        mysql.get_db().commit()

        return redirect(url_for("patients.patients"))


@patientsRoutes.route('/patients/edit', methods=['GET', 'POST'])
@loginRequired
def patientsEdit():
    if request.method == "GET":
        return redirect(url_for("root.nucleo"))

    if request.method == "POST":
        cursor = mysql.get_db().cursor()

        cursor.execute("""
            UPDATE `com_nucleo_medico_pacientes` SET `own`=%s,`name`=%s,`birthday`=%s,`sexo`=%s,`email`=%s,`ocupacion`=%s,`escolaridad`=%s,`curp`=%s,`estado_civil`=%s,`domicilio`=%s,`colonia`=%s,`estado`=%s,`municipio`=%s,`celular`=%s,`tel_casa`=%s,`tel_oficina`=%s WHERE `id`= %s
            """, (session['id'],  request.form["name"], request.form["birthday"], request.form["gender"], request.form["email"], request.form["occupation"], request.form["scholarship"], request.form["id"], request.form["mStatus"], request.form["address"], request.form["suburb"], request.form["government"], request.form["city"], request.form["phone"], request.form["hPhone"], request.form["oPhone"], request.form["toEdit"]))

        mysql.get_db().commit()

        return redirect(url_for("patients.patients"))


@patientsRoutes.route('/patients/delete', methods=['GET', 'POST'])
@loginRequired
def patientsDelete():
    if request.method == "GET":
        return redirect(url_for("root.nucleo"))

    if request.method == "POST":
        cursor = mysql.get_db().cursor()

        cursor.execute("""
            UPDATE `com_nucleo_medico_pacientes` SET `delete`= 1 WHERE `id`= %s
            """, (request.form['value']))

        mysql.get_db().commit()

        return redirect(url_for("patients.patients"))


@patientsRoutes.route('/patients/restore', methods=['GET', 'POST'])
@loginRequired
def patientsRestore():
    if request.method == "GET":
        return redirect(url_for("root.nucleo"))

    if request.method == "POST":
        cursor = mysql.get_db().cursor()

        cursor.execute("""
            UPDATE `com_nucleo_medico_pacientes` SET `delete`= 0 WHERE `id`= %s
            """, (request.form['value']))

        mysql.get_db().commit()

        return redirect(url_for("patients.patients"))
