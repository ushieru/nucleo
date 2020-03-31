from flask import session, redirect, url_for
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
