#!/usr/bin/python3
"""Defines the State class with a relationship to its City objects."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents a row of the states table and its linked cities."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", lazy="joined",
                          order_by="City.id", cascade="all, delete-orphan")
