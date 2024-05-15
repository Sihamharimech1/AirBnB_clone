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

s = BaseModel()
s.name = "My First Model"
s.number = 89
s.save()
print(s)