from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class PaisForm(FlaskForm):
    nombre = StringField('NOMBRE')
    submit = SubmitField('GUARDAR')