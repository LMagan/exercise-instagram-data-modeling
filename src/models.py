import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))

class Comment(Base):
    __tablename__ ='comment'

    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(50), nullable=True)
    author_id = Column(Integer, ForeignKey('user.user_id'))
    post_id = Column(Integer, ForeignKey('post.post_id'))

class Media(Base):
    __tablename__ = 'media'

    media_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    type = Column(String(20), nullable=False)
    url = Column(String(20), nullable=True)

class Follower(Base):
    __tablename__ = 'follower'

    follower_id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.user_id'))
    user_to_id = Column(Integer, ForeignKey('user.user_id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
