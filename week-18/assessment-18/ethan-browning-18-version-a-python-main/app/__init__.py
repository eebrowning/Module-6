from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from app.config import Configuration
from app.forms import NewInstrument
from app.models import db, Instrument

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def main():
    return render_template('main_page.html')


@app.route('/new_instrument')
def get_new_instrument():
    form = NewInstrument()

    return render_template('simple_form.html', form=form)


@app.route('/new_instrument', methods=["POST"])
def post_new_instrument():
    form = NewInstrument()

    if form.validate_on_submit():
        data = form.data
        print(data, 'this is the data')
        instrument = {
            "date_bought": data['date_bought'],
            "nickname": data['nickname'],
            "year": data['year'],
            "maker": data['maker'],
            "type": data['type'],
            "used": data['used']
        }
        new_instrument = Instrument(**instrument)
        db.session.add(new_instrument)
        db.session.commit()
        return redirect('/instrument_data')
    return "<h1>Bad Data</h1>"



@app.route('/instrument_data')
def instrument_data():
    instruments= Instrument.query.all()

    return render_template('simple_form_data.html', instruments=instruments)
