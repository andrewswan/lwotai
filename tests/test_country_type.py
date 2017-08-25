from unittest import TestCase

from lwotai.countries.types import CountryType


class CountryTypeTest(TestCase):

    def test_repr(self):
        # Set up
        name = "theName"
        country_type = CountryType(name)

        # Invoke
        repr = "%s" % country_type

        # Check
        self.assertEqual(name, repr)
