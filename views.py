from flask import render_template
from forms import NumbersForm

from app import app

@app.route("/")
def get_input():
    form = NumbersForm()
    return render_template('home.html', title='GetNumber', form=form)
