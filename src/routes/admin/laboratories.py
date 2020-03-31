from flask import Blueprint, render_template, request, redirect, url_for

laboratoriesRoutes = Blueprint('laboratories', __name__)

labs = [["0", "Lab1 Test", "Lab1@test.com", "address # 00", "0000000000", "1"],
        ["1", "Lab2 Test", "Lab2@test.com", "address # 11", "0000000000", "0"],
        ["2", "Lab3 Test", "Lab3@test.com", "address # 22", "0000000000", "0"],
        ["3", "Lab4 Test", "Lab4@test.com", "address # 33", "0000000000", "0"],
        ["4", "Lab5 Test", "Lab5@test.com", "address # 44", "0000000000", "1"]]
labscount = 5


@laboratoriesRoutes.route('/laboratories')
def laboratories():
    return render_template('app/modules/admin/laboratories.html', labs=labs)

@laboratoriesRoutes.route('/laboratories/add', methods=['GET', 'POST'])
def laboratoriesAdd():
    global labscount
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        labs.append([str(labscount), request.form.get("name"), request.form.get(
            "email"), request.form.get("address"), request.form.get("phone"), "0"])
        labscount += 1
        return redirect(url_for("laboratories.laboratories"))

@laboratoriesRoutes.route('/laboratories/edit', methods=['GET', 'POST'])
def laboratoriesEdit():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for lab in labs:
            if lab[0] == request.form.get("id"):
                lab[1] = request.form.get("name")
                lab[2] = request.form.get("email")
                lab[3] = request.form.get("address")
                lab[4] = request.form.get("phone")
                return redirect(url_for("laboratories.laboratories"))

@laboratoriesRoutes.route('/laboratories/delete', methods=['GET', 'POST'])
def laboratoriesDelete():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for lab in labs:
            if lab[0] == request.form.get("value"):
                lab[5] = "1"
                return redirect(url_for("laboratories.laboratories"))

@laboratoriesRoutes.route('/laboratories/restore', methods=['GET', 'POST'])
def laboratoriesRestore():
    if request.method == "GET":
        return redirect(url_for("control.nucleo"))

    if request.method == "POST":
        for lab in labs:
            if lab[0] == request.form.get("value"):
                lab[5] = "0"
                return redirect(url_for("laboratories.laboratories"))