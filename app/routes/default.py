from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user

from app import app
from datetime import timedelta, date

@app.route("/")
@login_required
def main():
    mock = {}
    for item in range(5):
        event_date = date.today() + timedelta(days=item)
        date_str = event_date.strftime("%d %B")
        mock[date_str] = [ 'event 1', 'event 2']
    print(mock)
    return render_template('main.html', iterable=mock)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
