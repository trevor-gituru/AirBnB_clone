import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), type("s"))
