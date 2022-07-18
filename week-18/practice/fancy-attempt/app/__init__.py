from flask import Flask, redirect, render_template
from app.forms import SimpleForm
from app.config import Configuration
from app.models import SimplePerson, db
from flask_migrate import Migrate

app= Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('main_page.html')

@app.route("/simple-form")
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)

@app.route('/simple-form', methods=["POST"])
def simple_form_post():
    form = SimpleForm()
    if form.validate_on_submit():
        person={
            "name": form.data["name"],
            "age": form.data["age"],
            "bio": form.data["bio"],
        }
        simple_person= SimplePerson(**person)

        return redirect("/")
    return "<h1>Bad Data</h1>"

@app.route('/simple-form-data')
def simple_form_data():
    pass
