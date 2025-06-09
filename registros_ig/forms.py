from flask_wtf import FlaskForm
from wtforms import DateField, StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length


class MovementsForms(FlaskForm):
    date = DateField("Fecha",validators=[DataRequired(message="La fecha es requerida")])
    concept = StringField("concepto",validators=[DataRequired(message="El concepto es requerido"),Length(min=4,message="más de cuatro caracteres")])
    quantity = FloatField("Monto",validators=[DataRequired(message="La cantidad es requerida")])

    submit = SubmitField("Acepar")
