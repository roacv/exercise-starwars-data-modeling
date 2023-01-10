import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
     __tablename__ = 'user'
     # Here we define columns for the table person
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     name = Column(String(250), nullable=False)
     lastname = Column(String(250), nullable=False)
     datecrea = Column(DateTime(timezone=True), nullable=False)
     email = Column(String(250), nullable=False)
     password = Column(String(8), nullable=False)
     favs = relationship("Fav",backref="user")

class Planet(Base):
     __tablename__ = 'planets'
     # Here we define columns for the table person
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     name = Column(String(250), nullable=False)
     obs = Column(String(250), nullable=False)
     climate = Column(String(50), nullable=False)
     terrain = Column(String(50), nullable=False)
     population = Column(Integer, nullable=False)
     surfacew = Column(Integer, nullable=False)
     diameter = Column(Integer, nullable=False)
     orbitalp = Column(Integer, nullable=False)
     rotationp = Column(Integer, nullable=False)
     gravity = Column(String(50), nullable=False)
     description = Column(Text, nullable=False)

class Character(Base):
     __tablename__ = 'characters'
     # Here we define columns for the table person
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     name = Column(String(250), nullable=False)
     obs = Column(String(250), nullable=False)
     birth = Column(String(50), nullable=False)
     gender = Column(String(50), nullable=False)
     height = Column(Integer, nullable=False)
     mass = Column(Integer, nullable=False)
     haircolor = Column(String(50), nullable=False)
     eyecolor = Column(String(50), nullable=False)
     skincolor = Column(String(50), nullable=False)
     description = Column(Text, nullable=False)

class Fav(Base):
     __tablename__ = 'favs'
     # Here we define columns for the table person
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     tipo = Column(String(1), nullable=False)
     user_id = Column(String(250), ForeignKey("user.id"), nullable=True)
     planet_id = Column(String(250), ForeignKey("planets.id"), nullable=True)
     character_id = Column(String(50), ForeignKey("characters.id"), nullable=False)
     planet = relationship("Planet",backref="favs")
     character = relationship("Character",backref="favs")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
