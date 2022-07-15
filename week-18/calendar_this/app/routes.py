from flask import Blueprint, render_template, url_for, redirect
import os
import psycopg2
from app.forms import AppointmentForm
from datetime import datetime, timedelta

bp = Blueprint('main', __name__, '/')


CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route("/", methods=["GET", "POST"])
def main():
    d = datetime.now()
    return redirect(url_for(".daily", year=d.year, month=d.month, day=d.day))

    
@bp.route('/<int:year>/<int:month>/<int:day>', methods=['GET','POST'])
def daily(year, month, day):
    form = AppointmentForm()
    if form.validate_on_submit():
      with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
         with conn.cursor() as curs:
            params = {
                'name': form.name.data,
                'start_datetime': datetime.combine(form.start_datetime_date.data, form.start_datetime_time.data),
                'end_datetime': datetime.combine(form.end_datetime_date.data, form.end_datetime_time.data),
                'description': form.description.data,
                'private': form.private.data
                        }
            curs.execute("INSERT INTO appointments (name, start_datetime, end_datetime, description, private) VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s); ", params)
    
    

    # Create a psycopg2 connection with the connection parameters
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        # Create a cursor from the connection
      with conn.cursor() as curs:
        day= datetime(year,month,day)
        daydiff=timedelta(days=1)
        next_day= day + daydiff
        curs.execute(
            """
        SELECT id, name, start_datetime, end_datetime
        FROM appointments
        WHERE start_datetime BETWEEN %(day)s AND %(next_day)s
        ORDER BY start_datetime
        """,
        {
            "day":day,
            "next_day": next_day
        }
        )
        result= curs.fetchall()
        new_result= []
        for appt in result:
            new={}
            new['id']= appt[0]
            new['name']= appt[1]
            new['start_datetime']= appt[2].strftime("%H:%M")
            new['end_datetime']= appt[3].strftime("%H:%M")
            new_result.append(new)


        print(new_result)

        return render_template("main.html", rows=new_result, form=form)
