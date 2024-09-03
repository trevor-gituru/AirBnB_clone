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
