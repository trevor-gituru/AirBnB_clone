from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        if (len(kwargs) != 0): 
            for kw in kwargs:
                if (kw != "__class__"):
                    setattr(self, kw, kwargs[kw])
                if (kw == "created_at" or kw == "updated_at"):
                    setattr(self,
                            kw,
                            datetime.strptime(kwargs[kw], "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = instance_dict["created_at"].isoformat() 
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        return instance_dict
