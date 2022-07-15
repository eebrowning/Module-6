from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired
from map.map import map



airports= [city for city in map]
# print(airports)



class ShippingForm(FlaskForm):
    sender_name= StringField('Sender Name', validators=[DataRequired()])
    recipient_name= StringField('Recipient Name', validators=[DataRequired()])
    origin= SelectField('Origin', choices=airports, validators=[DataRequired()])
    destination= SelectField('Destination',choices=airports , validators=[DataRequired()])
    express= BooleanField('Express Shipping', validators=[DataRequired()])
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
