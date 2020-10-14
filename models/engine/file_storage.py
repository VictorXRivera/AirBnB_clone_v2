#!/usr/bin/python3
"""File_Storage Class"""
import json
import models


class FileStorage:
    """
    Serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returning dictionary.
        """
        if cls is None:
            return self.__objects
        else:
            my_dict = {}
            for r, v in self.__objects.items():
                name = r.split('.')
                if name[0] in str(cls):
                    my_dict[r] = v
            return my_dict

    def new(self, obj):
        """
        New object method.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes __objects attribute to JSON file.
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as hb:
            json.dump(objects_dict, hb)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as hb:
                FileStorage.__objects = json.load(hb)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object.
        """
        copy_storage = dict(FileStorage.__objects)
        desired_key = obj
        for key, val in copy_storage.items():
            if val == desired_key:
                del(obj)
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """
        Deserializes JSON file to objects.
        """
        self.reload()
