#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances

    #### Private Class Attributes:

    - __file_path: `(string)` - path to the JSON file
    - __objects: `(dictionary)` - empty but will store all
    objects by <class name>.id

    #### Public instance methods:

    - all(self): returns the dictionary __objects
    - new(self, obj): sets in __objects the obj with key <obj class name>.id
    - save(self): serializes __objects to the JSON file (path: __file_path)
    """
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        #### Returns:
        `json`: the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)
