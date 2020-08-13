#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                cascade="all, delete-orphan",
                backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """ Cities method """
            city_item = []
            for item in models.storage.all(City).values():
                if item.state_id == self.id:
                    city_item.append(item)
            return city_item
