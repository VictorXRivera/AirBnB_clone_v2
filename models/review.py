#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Project 9 - Review class with updated attributes
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
