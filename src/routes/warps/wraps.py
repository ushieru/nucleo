from flask import session, redirect, url_for, request
from functools import wraps


def loginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('name'):
            pass
        else:
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
