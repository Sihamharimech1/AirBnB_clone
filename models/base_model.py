#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        id_base = uuid.uuid4()
        if kwargs:
            if(kwargs['updated_at']):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         "%Y-%m-%dT%H:%M:%S.%f")
            if(kwargs['created_at']):
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if(key == '__class__'):
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(id_base)
            self.created_at = datetime.now()
            created_time = self.created_at
            self.updated_at = created_time
            storage.new(self)


    def __str__(self):
        class_name = str(self.__class__.__name__)
        class_dict = str(self.__dict__)
        return f"[{class_name}] ({self.id}) {class_dict}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_vol = self.__dict__.copy()
        dict_vol['__class__'] = self.__class__.__name__
        dict_vol['created_at'] = self.created_at.isoformat()
        dict_vol['updated_at'] = self.updated_at.isoformat()
        return dict_vol

""" Testiing"""

