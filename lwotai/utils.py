class Utils(object):
    """Static utility methods"""
    def __init__(self):
        pass

    @staticmethod
    def require_type_or_none(value, required_type):
        """
        Asserts that the given value is either of the given type or is None
        :param value: the value to check
        :param required_type: the required type
        :return: the checked value
        """
        if value is None:
            return value
        return Utils.require_type(value, required_type)

    @staticmethod
    def require_type(value, required_type):
        """
        Asserts that the given value is of the given type
        :param value: the value to check
        :param required_type: the required type
        :return: the checked value
        """
        assert isinstance(value, required_type)
        return value

    @staticmethod
    def count(iterable, predicate):
        """
        Counts the items in the given iterable that match the given predicate
        :param iterable the iterable to filter
        :param predicate a function that takes one item and returns a boolean
        """
        return sum(1 for item in iterable if predicate(item))

    @staticmethod
    def find(iterable, predicate):
        """Returns the elements of the given iterable that match the given predicate"""
        return [item for item in iterable if predicate(item)]

    @staticmethod
    def getUserYesNoResponse(prompt):
        """Prompts the user for a yes/no answer (returns true or false)"""
        while True:
            user_input = raw_input(prompt)
            if "yes".startswith(user_input.lower()):
                return True
            elif "no".startswith(user_input.lower()):
                return False
            else:
                print "Enter y or n."
                print ""

    @staticmethod
    def choose_option(prompt, options):
        """Prompts the user to choose from the given options. Returns a number from 1 to the length of that list."""
        print prompt
        for number, option in enumerate(options):
            print "(" + str(number + 1) + ") " + option
        while True:
            input_str = raw_input("Enter choice: ")
            input_int = int(input_str)
            if 1 <= input_int <= len(options):
                return input_int
            else:
                print "Please enter a number from 1 to", len(options)
