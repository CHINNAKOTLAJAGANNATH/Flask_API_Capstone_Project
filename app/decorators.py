
from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first', 'info')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)

    return decorated_function