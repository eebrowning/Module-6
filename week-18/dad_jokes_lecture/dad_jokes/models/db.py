from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db= SQLAlchemy()
likes = db.Table(
    'likes',
    db.Model.metadata,
    db.Column('users', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('jokes',db.Integer, db.ForeignKey('jokes.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'

    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique=True)
    password= db.Column(db.String(50), nullable=False)
    
    # relationships - many jokes to one user
    jokes= db.relationship('Joke',  back_populates='user')
    # look up uselist?
    # jokes= db.relationship('Joke', uselist=False, back_populates='user')
    author_likes= db.relationship('Joke', 
        secondary= likes, 
        back_populates= 'joke_likes',
        cascade='all, delete'
    )

  

class Joke(db.Model):
    __tablename__= 'jokes'
    
    id= db.Column(db.Integer, primary_key= True)
    joke_body= db.Column(db.String(255), nullable=False)
    punchline= db.Column(db.String(255), nullable=False)
    rating= db.Column(db.String(10), nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # relationships -   user has many jokes
    user= db.relationship('User', back_populates="jokes")
