
from flask_login import login_required
from flask import Blueprint, render_template, url_for, redirect

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
        return render_template("orders.html")
        # return render_template("orders.html", form=form)
