from flask import render_template, redirect, request
from forms import NumbersForm

from app import app

@app.route("/", methods=['GET', 'POST'])
def get_input():
    form = NumbersForm()
    if request.method == 'POST':
        return redirect('json')
    else:
        return render_template('home.html', title='GetNumber', form=form)

@app.route("/json")
def get_json():
    return 'json'
