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
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        if(os.path.exists(self.__file_path)):
            self.__objects = json.load(open("self.__file_path", "r"))