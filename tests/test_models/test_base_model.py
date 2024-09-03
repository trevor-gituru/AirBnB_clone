import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        # Create an instance of BaseModel
        base_model = BaseModel()
        
        # Capture the current updated_at timestamp
        old_updated_at = base_model.updated_at
        
        # Sleep for a short time to ensure the timestamp changes
        sleep(0.1)
        
        # Call the save() method
        base_model.save()
        
        # Check if updated_at has been updated
        self.assertNotEqual(old_updated_at, base_model.updated_at)
        self.assertTrue(base_model.updated_at > old_updated_at)
        self.assertIsInstance(base_model.updated_at, datetime)
    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
        }
    
    def test_to_dict(self):
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Get the dictionary representation of the instance
        base_model_dict = base_model.to_dict()

        # Check if the returned dictionary contains all expected keys
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertIn('__class__', base_model_dict)

       # Check if 'created_at' and 'updated_at' are in ISO format
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)
        try:
            datetime.fromisoformat(base_model_dict['created_at'])
            datetime.fromisoformat(base_model_dict['updated_at'])
        except ValueError:
            self.fail("to_dict() does not convert datetime objects to ISO format")

    def test_str(self):
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Get the string representation of the instance
        base_model_str = str(base_model)

        # Expected format: [BaseModel] (<id>) <__dict__>
        expected_str = f"[{base_model.__class__.__name__}] ({base_model.id}) {base_model.__dict__}"

        # Check if the string matches the expected format
        self.assertEqual(base_model_str, expected_str)
