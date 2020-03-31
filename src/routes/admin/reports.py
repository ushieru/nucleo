from flask import Blueprint, render_template, request, redirect, url_for, send_file

reportsRoutes = Blueprint('reports', __name__)

@reportsRoutes.route('/reports')
def reports():
    return render_template('app/modules/admin/reports.html')

@reportsRoutes.route('/report')
def download():
    return send_file('./data/reports/demo.pdf', attachment_filename='demo.pdf')