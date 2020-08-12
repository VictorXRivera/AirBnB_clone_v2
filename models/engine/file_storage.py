#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Project 5 - update all to return list of objects of one type of class
                  - If class exists, initialize a dictionary helper to 
                    update dictionary for printing.
                  - For key, values specifies the items stored for the 
                    __objects in the FileStorage class
                  - If cls has a __name__ in key, update key's values using
                    dictionary help else return __objects in FileStorage class
        """
        if cls is not None:
            dict_help = {}
            for key, values in FileStorage.__objects.items():
                if(cls.__name__ in key):
                    dict_help.update({key: values})
            return dict_help
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Project 5 - delete obj from __objects if it's inside
                  - temp helps format (ie. name.id) for deletion
        """
        if obj is not None:
            temp = (type(obj).__name__) + '.' + obj.__dict__['id']
            del self.__objects[temp]
