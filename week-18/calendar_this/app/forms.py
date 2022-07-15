from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired,ValidationError
from datetime import datetime


class AppointmentForm(FlaskForm):
    name= StringField('name',  validators=[DataRequired()])
    start_datetime_date= DateField('start_date', validators=[DataRequired()])
    start_datetime_time= TimeField('start_time', validators=[DataRequired()])
    end_datetime_date= DateField('end_date', validators=[DataRequired()])
    end_datetime_time= TimeField('end_time', validators=[DataRequired()])
    description= TextAreaField('description', validators=[DataRequired()])
    private= BooleanField('private')
    submit= SubmitField("Add appointment")

    def validate_end_datetime_date(form, field):
        start = datetime.combine(form.start_datetime_date.data, form.start_datetime_time.data)
        end = datetime.combine(field.data, form.end_datetime_time.data)
        startday= form.start_datetime_date.data
        endday= field.data
        if start >= end:
            msg = "End date/time must come after start date/time"
            raise ValidationError(msg)
        if startday != endday :
            raise ValidationError('Appointment must start and end on same day')
