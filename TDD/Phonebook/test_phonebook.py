import unittest
from phonebook import Phonebook

class PhonebookTestCase(unittest.TestCase):
    """ TestCases for testing the Phonebook behaviours """

    def setUp(self):
        self.phonebook = Phonebook()
        self.contact1 = ("Bob", "254700")
        self.contact2 = ("Annie", "12347")
        self.contact3 = ("Lemmah", "123")
        self.contact4 = ("Claris", "01234")

    def test_phonebook_can_add_a_new_contact(self):
        """ Assert that contacts can be created within the phonebook """
        save_contact = self.phonebook.add(*self.contact1)
        # Test for a success message
        self.assertEqual(save_contact,
                "Bob has been added to your list of contacts")
        self.assertIn(self.phonebook.contacts, "Bob")

    def test_phonebook_can_lookup_contacts(self):
        """ Assert contacts can be looked up """
        self.phonebook.add(*self.contact1)
        bob_number = self.phonebook.lookup("Bob")
        self.assertEqual(bob_number, self.contact1[1])

    def test_phonebook_can_delete_a_contact(self):
        """ Assert that contacts can be delete from the phonebook """
        self.phonebook.add(*self.contact1)
        self.phonebook.add(*self.contact2)
        self.phonebook.add(*self.contact3)
        delete_bob = self.phonebook.delete("Bob")
        self.assertEqual(delete_bob,
                "Bob has been deleted from your contacts")

if __name__ == "__main__":
    unittest.main()
