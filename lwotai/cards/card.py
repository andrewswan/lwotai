class Card(object):
    """The superclass of all card classes"""

    def __init__(self, number, card_type, name, ops, remove, mark, lapsing, puts_cell=False):
        assert card_type in ["Jihadist", "Unassociated", "US"]
        assert name
        assert number > 0
        assert 1 <= ops <= 3
        self.__puts_cell = puts_cell
        self.__type = card_type
        self.lapsing = lapsing
        self.mark = mark
        self.name = name
        self.number = number
        self.ops = ops
        self.remove = remove

    def get_type(self):
        """Returns the side with which this card is associated: 'Jihadist', 'US', or 'Unassociated'"""
        return self.__type

    def playable(self, side, app, ignore_itjihad):
        """Whether this card's event is playable by the given side"""
        if self.__type == "US" and side == "Jihadist":
            return False
        elif self.__type == "Jihadist" and side == "US":
            return False
        elif side == "Jihadist" and "The door of Itjihad was closed" in app.lapsing and not ignore_itjihad:
            return False
        return self._really_playable(side, app, ignore_itjihad)

    def is_playable_non_us_event(self, app):
        return self.__type != "US" and self.playable("Jihadist", app, False)

    def is_playable_us_event(self, app):
        return self.__type == "US" and self.playable("US", app, False)

    def is_unassociated(self):
        return self.__type == "Unassociated"

    def _really_playable(self, _side, _app, _ignore_itjihad):
        """Indicates whether this card is playable, assuming the side is valid; subclasses to override"""
        return True

    def puts_cell(self):
        """Whether this card's event places a cell; not for overriding"""
        return self.__puts_cell

    def play_event(self, side, app):
        """Executes this card's event as the given side (US or Jihadist); not for overriding"""
        app.output_to_history("Card played for Event.")
        self.do_play_event(side, app)
        if self.remove:
            app.output_to_history("Remove card from game.", True)
        if self.mark:
            app.output_to_history("Place marker for card.", True)
        if self.lapsing:
            app.output_to_history("Place card in Lapsing.", True)

    def do_play_event(self, side, app):
        """Executes the event logic; for subclasses to override"""
        pass
