#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel):
    """ The city class, contains state ID and name
    However if a state is deleted then the city associated
    with the state will be deleted as well
    """

    __tablename__ = 'cities'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship('Place', cascade='all, delete-orphan',
                            backref='cities')
    else:
        name = ""
        state_id = ""
