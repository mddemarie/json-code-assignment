from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class NumbersForm(FlaskForm):
    max_num = IntegerField('UserNumber', validators=[DataRequired()])
    submit = SubmitField('Submit')