#!/usr/bin/python3
"""
Establish link to table in database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state entity in the database.

    Attributes:
        id (int): The unique identifier for the state (primary key).
        name (str): The name of the state, limited to 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
