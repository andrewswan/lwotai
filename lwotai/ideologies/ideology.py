class Ideology(object):
    """One of the ideologies that the Jihadist AI can have."""

    def __eq__(self, o):
        return o.name and self.name() == o.name()

    def __ne__(self, o):
        return not o.name or self.name() != o.name()

    def name(self):
        pass
