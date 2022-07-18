from tokenize import String
from flask_wtf import FlaskForm
from wtforms.fields import(
    IntegerField, StringField, SelectField, SubmitField, BooleanField, DateField)
from wtforms.validators import (DataRequired)


class SimpleForm(FlaskForm):
    date_bought = DateField('Date Bought', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    year = IntegerField('Year')
    maker = StringField('Maker')
    type = SelectField(
        'Type', choices=['Other', 'String', 'Woodwind', 'Brass', 'Percussion'])
    used = BooleanField('Used', validators=[DataRequired()])
