from flask import session, redirect, url_for, request, flash
from functools import wraps


def loginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('name'):
            pass
        else:
            flash(u'You need sign in first', 'Error')
            return redirect(url_for("index.home"))
        return f(*args, **kwargs)
    return decorated_function


def isDoctor(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('isDoctor'):
            pass
        else:
            flash("You don't have permission to access this module", 'Error')
            return redirect(url_for("index.home"))
        return f(*args, **kwargs)
    return decorated_function


def onlyPOST(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method != "POST":
            return redirect(url_for("index.home"))
        return f(*args, **kwargs)
    return decorated_function
