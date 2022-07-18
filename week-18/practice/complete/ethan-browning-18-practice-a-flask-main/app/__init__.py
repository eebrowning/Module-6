from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from app.config import Configuration
from app.forms import SimpleForm
from app.models import db, SimplePerson

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
def index():
    # return "<h1>Practice Assessment</h1>"
    return render_template("main_page.html")


@app.route("/simple-form", methods=["GET"])
def form_get():
    form = SimpleForm()
    # return "<h1>Practice Assessment</h1>"
    return render_template("simple_form.html", form=form)


@app.route("/simple-form", methods=["POST"])
def form_post():
    form = SimpleForm()
    # print(form.errors, "this is the form.errors data")

    if form.validate_on_submit():
        data = form.data
        person = {
            "name": data['name'],
            "age": data['age'],
            "bio": data['bio'],
        }
        new_person = SimplePerson(**person)
        db.session.add(new_person)
        db.session.commit()

        return redirect('/')
    return "<h1>Bad Data</h1>"


@app.route('/simple-form-data', methods=["GET"])
def form_data():
    simpletons = SimplePerson.query.all()

    return render_template("simple_form_data.html", simpletons=simpletons)
