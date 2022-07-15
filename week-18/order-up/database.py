from dotenv import load_dotenv


load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table


with app.app_context():
    db.drop_all()
    db.create_all()
# emps
    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()
# food
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    db.session.add(beverages)
    db.session.add(entrees)
    db.session.add(sides)
    db.session.add(dinner)
    db.session.add(fries)
    db.session.add(drp)
    db.session.add(jambalaya)

    db.session.commit()
#tables
    table0= Table(number=0,capacity=100)
    table1= Table(number=1,capacity=100)
    table2= Table(number=2,capacity=100)
    table3= Table(number=3,capacity=100)
    table4= Table(number=4,capacity=100)
    table5= Table(number=5,capacity=100)
    table6= Table(number=6,capacity=100)
    table7= Table(number=7,capacity=100)
    table8= Table(number=8,capacity=100)
    table9= Table(number=9,capacity=100)
    db.session.add(table0)
    db.session.add(table1)
    db.session.add(table2)
    db.session.add(table3)
    db.session.add(table4)
    db.session.add(table5)
    db.session.add(table6)
    db.session.add(table7)
    db.session.add(table8)
    db.session.add(table9)
    db.session.commit()
