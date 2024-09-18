from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class CategoriaForm(FlaskForm):
    nombre = StringField('NOMBRE')
    submit = SubmitField('Guardar')