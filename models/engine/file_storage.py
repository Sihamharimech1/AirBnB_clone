#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        unique_key = type(obj).__name__ + '.' + obj.id
        self.__objects[unique_key] = obj

    def save(self):
        serializable_version = {}
        for key, obj in FileStorage.__objects.items():
                serializable_version[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_version, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass