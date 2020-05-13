from flask import Blueprint, render_template, request, redirect, url_for, session
from src.routes.warps.wraps import loginRequired
from src import mysql

farmaciaRoutes = Blueprint('farmacia', __name__)


@farmaciaRoutes.route('/', methods=['GET', 'POST'])
@loginRequired
def farmacia():

    return render_template('app/farmacia/farmacia.html')