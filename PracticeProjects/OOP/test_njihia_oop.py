import unittest
from njihia_oop import *


class oopTest(unittest.TestCase):

    def test_person_instance(self):
        tenant1 = Tenant('Sue', 'Jackson', 10000)
        owner1 = Property_owner('Ian', 'Smith', [tenant1])
        self.assertIsInstance(
            owner1, Person,
            msg='The object should be an instance of the `Person` class')

    def test_object_type(self):
        tenant1 = Tenant('Sue', 'Jackson', 10000)
        self.assertTrue(
            (type(tenant1) is Tenant),
            msg='The object should be a type of `Tenant`')


if __name__ == '__main__':
    unittest.main()
