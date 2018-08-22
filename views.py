from flask import render_template

from app import app

@app.route("/")
def get_input():
    return render_template('home.html', title='GetNumber')
