import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **Kwargs):
        id_base = uuid.uuid4()
        self.id = str(id_base)
        self.created_at = datetime.now()
        created_time = self.created_at
        self.updated_at = created_time
        if Kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        class_name = str(self.__class__.__name__)
        class_dict = str(self.__dict__)
        return f"[{class_name}] ({self.id}) {class_dict}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_vol = self.__dict__
        dict_vol['__class__'] = self.__class__.__name__
        dict_vol['created_at'] = self.created_at.isoformat()
        dict_vol['updated_at'] = self.updated_at.isoformat()
        return dict_vol
