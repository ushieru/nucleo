from flask import Blueprint, render_template, request, redirect, url_for

medicinesRoutes = Blueprint('medicines', __name__)

provs = [["0", "Prov1 Test", "Prov1@test.com", "address # 00", "0000000000", "0"],
         ["1", "Prov2 Test", "Prov2@test.com", "address # 11", "0000000000", "0"],
         ["2", "Prov3 Test", "Prov3@test.com", "address # 22", "0000000000", "0"],
         ["3", "Prov4 Test", "Prov4@test.com", "address # 33", "0000000000", "1"],
         ["4", "Prov5 Test", "Prov5@test.com", "address # 44", "0000000000", "1"]]

labs = [["0", "Lab1 Test", "Lab1@test.com", "address # 00", "0000000000", "1"],
        ["1", "Lab2 Test", "Lab2@test.com", "address # 11", "0000000000", "0"],
        ["2", "Lab3 Test", "Lab3@test.com", "address # 22", "0000000000", "0"],
        ["3", "Lab4 Test", "Lab4@test.com", "address # 33", "0000000000", "0"],
        ["4", "Lab5 Test", "Lab5@test.com", "address # 44", "0000000000", "1"]]

meds = [["0", "Medicine1 Test", "2052-09-01", "labs[1][1]", "provs[1][1]", "0"],
        ["1", "Medicine2 Test", "2052-09-01", "labs[3][1]", "provs[1][1]", "0"],
        ["2", "Medicine3 Test", "2052-09-01", "labs[3][1]", "provs[0][1]", "0"],
        ["3", "Medicine4 Test", "2052-09-01", "labs[1][1]", "provs[2][1]", "1"],
        ["4", "Medicine5 Test", "2052-09-01", "labs[2][1]", "provs[0][1]", "1"]]
medscount = 5

@medicinesRoutes.route('/medicines')
def medicines():
    return render_template('app/modules/admin/medicines.html', meds=meds, labs=labs, provs=provs)

@medicinesRoutes.route('/medicines/add', methods=['GET', 'POST'])
def medicinesAdd():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        global medscount
        meds.append([str(medscount), request.form.get("name"), request.form.get(
            "expiration"), request.form.get("laboratories"), request.form.get("providers"), "0"])
        medscount += 1
        return redirect(url_for("medicines.medicines"))

@medicinesRoutes.route('/medicines/edit', methods=['GET', 'POST'])
def medicinesEdit():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for med in meds:
            if med[0] == request.form.get("id"):
                med[1] = request.form.get("name")
                med[2] = request.form.get("expiration")
                med[3] = request.form.get("laboratories")
                med[4] = request.form.get("providers")
                return redirect(url_for("medicines.medicines"))

@medicinesRoutes.route('/medicines/delete', methods=['GET', 'POST'])
def medicinesDelete():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for med in meds:
            if med[0] == request.form.get("value"):
                med[5] = "1"
                return redirect(url_for("medicines.medicines"))

@medicinesRoutes.route('/medicines/restore', methods=['GET', 'POST'])
def medicinesRestore():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for med in meds:
            if med[0] == request.form.get("value"):
                med[5] = "0"
                return redirect(url_for("medicines.medicines"))