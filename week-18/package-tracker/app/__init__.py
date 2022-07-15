from tkinter import Pack
from flask import Flask, render_template, redirect, request
from flask_migrate import Migrate
from .config import Config
from .shipping_form import ShippingForm
from .models import db
from app.models import Package, db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    packages = Package.query.all()
    return render_template('package_status.html',packages=packages)


@app.route('/new_package', methods=["POST","GET"])
def new_package():
    form = ShippingForm() 
    if form.cancel.data:  # if cancel button is clicked, the form.cancel.data will be True
            return redirect('/')
    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect("/")
    

    return render_template('shipping_request.html', form=form)
