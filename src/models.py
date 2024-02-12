import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    usename = Column(String(100), nullable=False)
    firstname= Column(Integer,nullable=False)
    lastname = Column(String(50))
    email = Column(String(100), nullable = False)



class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type= Column(Enum())
    url = Column(String(50))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):
     __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     comment_text = Column(String(500))
     author_id = Column(Integer, ForeignKey('user.id'))
     post_id = Column(Integer, ForeignKey('post.id'))
     post = relationship(Post)
     user = relationship(User)

class Follower(Base):
     __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
     user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
     user_to_id = Column(Integer, ForeignKey('user.id'))
     user = relationship(User)


def to_dict(self):
        return {}
    
 
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
