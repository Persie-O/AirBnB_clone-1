#!/usr/bin/python3
"se model tests"" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """base_model class test"""

    @classmethod
    def setUpClass(cls):
        """class method setUp"""
        cls.base1 = BaseModel()
        cls.base1.name = "Base"
        cls.base1.my_number = 12

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """tests constructor"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "cannot work in database")

    def test_save(self):
        """ tests save """
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at', str])
        self.assertIsInstance(base1_dict['updated_at'], str])

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == "__main__":
    unittest.main()
