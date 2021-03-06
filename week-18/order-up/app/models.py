from flask_login import UserMixin  # New import
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Employee(db.Model, UserMixin):  # Your class definition
    __tablename__ = "employees"  # Mapping attributes, here

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model, UserMixin):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    items = db.relationship("MenuItem", back_populates="menu", cascade="all, delete")


class MenuItem(db.Model, UserMixin):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(
        db.Integer,
        db.ForeignKey("menus.id"),
        nullable=False,
    )
    menu_type_id = db.Column(
        db.Integer, db.ForeignKey("menu_item_types.id"), nullable=False
    )  # , ForeignKey('menus.id'))

    menu = db.relationship("Menu", back_populates="items")
    type = db.relationship("MenuItemType", back_populates="items")


class MenuItemType(db.Model, UserMixin):
    __tablename__ = "menu_item_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    items = db.relationship("MenuItem", back_populates="type", cascade="all, delete")


class Table(db.Model, UserMixin):
    __tablename__ = "tables"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False, unique=True)
    capacity = db.Column(db.String(20), nullable=False)
