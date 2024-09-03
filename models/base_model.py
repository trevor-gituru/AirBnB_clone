import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    self.__dict__)
    
    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = instance_dict["created_at"].isoformat() 
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        return instance_dict
