from flask import Blueprint, render_template, request, redirect, url_for

providersRoutes = Blueprint('providers', __name__)

provs = [["0", "Prov1 Test", "Prov1@test.com", "address # 00", "0000000000", "0"],
         ["1", "Prov2 Test", "Prov2@test.com", "address # 11", "0000000000", "0"],
         ["2", "Prov3 Test", "Prov3@test.com", "address # 22", "0000000000", "0"],
         ["3", "Prov4 Test", "Prov4@test.com", "address # 33", "0000000000", "1"],
         ["4", "Prov5 Test", "Prov5@test.com", "address # 44", "0000000000", "1"]]
provscount = 5

@providersRoutes.route('/providers')
def providers():
    return render_template('app/modules/admin/providers.html', provs=provs)

@providersRoutes.route('/providers/add', methods=['GET', 'POST'])
def providersAdd():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        global provscount
        provs.append([str(provscount), request.form.get("name"), request.form.get(
            "email"), request.form.get("address"), request.form.get("phone"), "0"])
        provscount += 1
        return redirect(url_for("providers.providers"))

@providersRoutes.route('/providers/edit', methods=['GET', 'POST'])
def providersEdit():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for prov in provs:
            if prov[0] == request.form.get("id"):
                prov[1] = request.form.get("name")
                prov[2] = request.form.get("email")
                prov[3] = request.form.get("address")
                prov[4] = request.form.get("phone")
                return redirect(url_for("providers.providers"))

@providersRoutes.route('/providers/delete', methods=['GET', 'POST'])
def providersDelete():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for prov in provs:
            if prov[0] == request.form.get("value"):
                prov[5] = "1"
                return redirect(url_for("providers.providers"))

@providersRoutes.route('/providers/restore', methods=['GET', 'POST'])
def providersRestore():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for prov in provs:
            if prov[0] == request.form.get("value"):
                prov[5] = "0"
                return redirect(url_for("providers.providers"))