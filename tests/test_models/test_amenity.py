#!/usr/bin/python3
"""tests for amenity class"""

import unittest
import os
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ amenity class test """

    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass_Amenity(self):
        """ tests if its subclass """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_check_docstring_Amenity(self):
        """ checks for decotsring """
        self.assertIsNotNone(Amenity.__doc__)

    def test_atrr_Amenity(self):
        """ checks availability of atrributes """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_to_dict_Amenity(self):
        """ tests for Amenity dict """
        self.assertEqual('to_dict' in dir(self.amenity), True)

    def test_save_Amenity(self):
        """ tests saving """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == "__main__":
    unittest.main()
