from flask import Blueprint, render_template, request, redirect, url_for

patientsRoutes = Blueprint('patients', __name__)

pats = [["0", "Uziel Cocolan Flores", "1997-12-29", "M", "uzielcocolan@gmail.com", "Estudiante",
         "Superior", "COFU971229HJCCLZ09", "ASD123FGH456", "Soltero", "Caanan # 00",
         "San Joaquin", "Jalisco", "Guadalajara", "3323314492", "n/a", "n/a", "0"],

        ["1", "Hector Ramirez Hernandez", "2002-05-13", "M", "hectorramirez@gmail.com", "Estudiante",
         "Media Superior", "RAHH020513HJCCLZ09", "ASD123FGH456", "Soltero", "Jordan # 00",
         "Hermosa Provincia", "Jalisco", "Guadalajara", "3346958172", "n/a", "n/a", "1"]]
patscount = 2

@patientsRoutes.route('/patients')
def patients():
    return render_template('app/modules/admin/patients.html', pats=pats)

@patientsRoutes.route('/patients/gestor', methods=['GET', 'POST'])
def patientsGestor():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        if request.form.get("value") == "-1":
            return "Search %s" % (request.form.get("search"))

        if request.form.get("value") == "0":
            return render_template('app/modules/admin/patientsadd.html', title="Add Patient", pat=[])
        else:
            for pat in pats:
                if pat[0] == request.form.get("id"):
                    return render_template('app/modules/admin/patientsadd.html', title="Edit Patient", pat=pat)

@patientsRoutes.route('/patients/add', methods=['GET', 'POST'])
def patientsAdd():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        global patscount
        pats.append([str(patscount), request.form.get("name"), request.form.get("birthday"), request.form.get("gender")[:1].upper(), request.form.get("email"), request.form.get("occupation"),
        request.form.get("scholarship"), request.form.get("id"), request.form.get("lin"), request.form.get("mStatus"), request.form.get("address"), request.form.get("suburb"), request.form.get("government"),
        request.form.get("city"), request.form.get("phone"), request.form.get("hPhone"), request.form.get("oPhone"), '0'])
        patscount += 1
        return redirect(url_for("patients.patients"))

@patientsRoutes.route('/patients/edit', methods=['GET', 'POST'])
def patientsEdit():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for pat in pats:
            if pat[0] == request.form.get("toEdit"):
                pat[1] = request.form.get("name")
                pat[2] = request.form.get("birthday")
                pat[3] = request.form.get("gender")[:1].upper()
                pat[4] = request.form.get("email")
                pat[5] = request.form.get("occupation")
                pat[6] = request.form.get("scholarship")
                pat[7] = request.form.get("id")
                pat[9] = request.form.get("mStatus")
                pat[10] = request.form.get("address")
                pat[11] = request.form.get("suburb")
                pat[12] = request.form.get("government")
                pat[13] = request.form.get("city")
                pat[14] = request.form.get("phone")
                pat[15] = request.form.get("hPhone")
                pat[16] = request.form.get("oPhone")
                return redirect(url_for("patients.patients"))

@patientsRoutes.route('/patients/delete', methods=['GET', 'POST'])
def patientsDelete():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for pat in pats:
            if pat[0] == request.form.get("value"):
                pat[17] = '1'
                return redirect(url_for("patients.patients"))

@patientsRoutes.route('/patients/restore', methods=['GET', 'POST'])
def patientsRestore():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for pat in pats:
            if pat[0] == request.form.get("value"):
                pat[17] = '0'
                return redirect(url_for("patients.patients"))
