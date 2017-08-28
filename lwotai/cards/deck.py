from lwotai.cards.card import Card
from lwotai.cards.jihadist.card48 import Card48
from lwotai.cards.jihadist.card49 import Card49
from lwotai.cards.jihadist.card50 import Card50
from lwotai.cards.us.card1 import Card1
from lwotai.cards.us.card11 import Card11
from lwotai.cards.us.card12 import Card12
from lwotai.cards.us.card13 import Card13
from lwotai.cards.us.card14 import Card14
from lwotai.cards.us.card15 import Card15
from lwotai.cards.us.card16 import Card16
from lwotai.cards.us.card17 import Card17
from lwotai.cards.us.card19 import Card19
from lwotai.cards.us.card2 import Card2
from lwotai.cards.us.card20 import Card20
from lwotai.cards.us.card21 import Card21
from lwotai.cards.us.card22 import Card22
from lwotai.cards.us.card23_24_25 import Card23and24and25
from lwotai.cards.us.card26 import Card26
from lwotai.cards.us.card27 import Card27
from lwotai.cards.us.card28 import Card28
from lwotai.cards.us.card29 import Card29
from lwotai.cards.us.card3 import Card3
from lwotai.cards.us.card30 import Card30
from lwotai.cards.us.card31 import Card31
from lwotai.cards.us.card32 import Card32
from lwotai.cards.us.card33 import Card33
from lwotai.cards.us.card34 import Card34
from lwotai.cards.us.card35 import Card35
from lwotai.cards.us.card36 import Card36
from lwotai.cards.us.card37 import Card37
from lwotai.cards.us.card38 import Card38
from lwotai.cards.us.card39 import Card39
from lwotai.cards.us.card4 import Card4
from lwotai.cards.us.card40 import Card40
from lwotai.cards.us.card41 import Card41
from lwotai.cards.us.card42 import Card42
from lwotai.cards.us.card43 import Card43
from lwotai.cards.us.card44 import Card44
from lwotai.cards.us.card45 import Card45
from lwotai.cards.us.card46 import Card46
from lwotai.cards.us.card47 import Card47
from lwotai.cards.us.card5 import Card5
from lwotai.cards.us.card6_7 import Card6and7
from lwotai.cards.us.card8_9_10 import Card8and9and10

CARDS = [
    Card1(),
    Card2(),
    Card3(),
    Card4(),
    Card5(),
    Card6and7(6),
    Card6and7(7),
    Card8and9and10(8),
    Card8and9and10(9),
    Card8and9and10(10),
    Card11(),
    Card12(),
    Card13(),
    Card14(),
    Card15(),
    Card16(),
    Card17(),
    Card(18, "US", "Intel Community", 2, False, False, False),
    Card19(),
    Card20(),
    Card21(),
    Card22(),
    Card23and24and25(23),
    Card23and24and25(24),
    Card23and24and25(25),
    Card26(),
    Card27(),
    Card28(),
    Card29(),
    Card30(),
    Card31(),
    Card32(),
    Card33(),
    Card34(),
    Card35(),
    Card36(),
    Card37(),
    Card38(),
    Card39(),
    Card40(),
    Card41(),
    Card42(),
    Card43(),
    Card44(),
    Card45(),
    Card46(),
    Card47(),
    Card48(),
    Card49(),
    Card50(),
    Card(51, "Jihadist", "FREs", 1, False, False, False),
    Card(52, "Jihadist", "IEDs", 1, False, False, False),
    Card(53, "Jihadist", "Madrassas", 1, False, False, False),
    Card(54, "Jihadist", "Moqtada al-Sadr", 1, True, True, False),
    Card(55, "Jihadist", "Uyghur Jihad", 1, True, False, False),
    Card(56, "Jihadist", "Vieira de Mello Slain", 1, True, True, False),
    Card(57, "Jihadist", "Abu Sayyaf", 2, True, True, False),
    Card(58, "Jihadist", "Al-Anbar", 2, True, True, False),
    Card(59, "Jihadist", "Amerithrax", 2, False, False, False),
    Card(60, "Jihadist", "Bhutto Shot", 2, True, True, False),
    Card(61, "Jihadist", "Detainee Release", 2, False, False, False),
    Card(62, "Jihadist", "Ex-KGB", 2, False, False, False),
    Card(63, "Jihadist", "Gaza War", 2, False, False, False),
    Card(64, "Jihadist", "Hariri Killed", 2, True, False, False),
    Card(65, "Jihadist", "HEU", 2, True, False, False),
    Card(66, "Jihadist", "Homegrown", 2, False, False, False),
    Card(67, "Jihadist", "Islamic Jihad Union", 2, True, False, False),
    Card(68, "Jihadist", "Jemaah Islamiya", 2, False, False, False),
    Card(69, "Jihadist", "Kazakh Strain", 2, True, False, False),
    Card(70, "Jihadist", "Lashkar-e-Tayyiba", 2, False, False, False),
    Card(71, "Jihadist", "Loose Nuke", 2, True, False, False),
    Card(72, "Jihadist", "Opium", 2, False, False, False),
    Card(73, "Jihadist", "Pirates", 2, True, True, False),
    Card(74, "Jihadist", "Schengen Visas", 2, False, False, False),
    Card(75, "Jihadist", "Schroeder & Chirac", 2, True, False, False),
    Card(76, "Jihadist", "Abu Ghurayb", 3, True, False, False),
    Card(77, "Jihadist", "Al Jazeera", 3, False, False, False),
    Card(78, "Jihadist", "Axis of Evil", 3, False, False, False),
    Card(79, "Jihadist", "Clean Operatives", 3, False, False, False),
    Card(80, "Jihadist", "FATA", 3, False, True, False),
    Card(81, "Jihadist", "Foreign Fighters", 3, False, False, False),
    Card(82, "Jihadist", "Jihadist Videos", 3, False, False, False),
    Card(83, "Jihadist", "Kashmir", 3, False, False, False),
    Card(84, "Jihadist", "Leak", 3, False, False, False),
    Card(85, "Jihadist", "Leak", 3, False, False, False),
    Card(86, "Jihadist", "Lebanon War", 3, False, False, False),
    Card(87, "Jihadist", "Martyrdom Operation", 3, False, False, False),
    Card(88, "Jihadist", "Martyrdom Operation", 3, False, False, False),
    Card(89, "Jihadist", "Martyrdom Operation", 3, False, False, False),
    Card(90, "Jihadist", "Quagmire", 3, False, False, False),
    Card(91, "Jihadist", "Regional al-Qaeda", 3, False, False, False),
    Card(92, "Jihadist", "Saddam", 3, False, False, False),
    Card(93, "Jihadist", "Taliban", 3, False, False, False),
    Card(94, "Jihadist", "The door of Itjihad was closed", 3, False, False, False),
    Card(95, "Jihadist", "Wahhabism", 3, False, False, False),
    Card(96, "Unassociated", "Danish Cartoons", 1, True, False, False),
    Card(97, "Unassociated", "Fatwa", 1, False, False, False),
    Card(98, "Unassociated", "Gaza Withdrawal", 1, True, False, False),
    Card(99, "Unassociated", "HAMAS Elected", 1, True, False, False),
    Card(100, "Unassociated", "Hizb Ut-Tahrir", 1, False, False, False),
    Card(101, "Unassociated", "Kosovo", 1, False, False, False),
    Card(102, "Unassociated", "Former Soviet Union", 2, False, False, False),
    Card(103, "Unassociated", "Hizballah", 2, False, False, False),
    Card(104, "Unassociated", "Iran", 2, False, False, False),
    Card(105, "Unassociated", "Iran", 2, False, False, False),
    Card(106, "Unassociated", "Jaysh al-Mahdi", 2, False, False, False),
    Card(107, "Unassociated", "Kurdistan", 2, False, False, False),
    Card(108, "Unassociated", "Musharraf", 2, False, False, False),
    Card(109, "Unassociated", "Tora Bora", 2, True, False, False),
    Card(110, "Unassociated", "Zarqawi", 2, False, False, False),
    Card(111, "Unassociated", "Zawahiri", 2, False, False, False),
    Card(112, "Unassociated", "Bin Ladin", 3, False, False, False),
    Card(113, "Unassociated", "Darfur", 3, False, False, False),
    Card(114, "Unassociated", "GTMO", 3, False, False, True),
    Card(115, "Unassociated", "Hambali", 3, False, False, False),
    Card(116, "Unassociated", "KSM", 3, False, False, False),
    Card(117, "Unassociated", "Oil Price Spike", 3, False, False, True),
    Card(118, "Unassociated", "Oil Price Spike", 3, False, False, True),
    Card(119, "Unassociated", "Saleh", 3, False, False, False),
    Card(120, "Unassociated", "US Election", 3, False, False, False)
]


class Deck(object):
    """The deck of cards in the game"""

    def __init__(self):
        self.cards = {}
        # Store the given list of cards in a dict, indexed by their number
        for card in CARDS:
            self.cards[card.number] = card

    def __len__(self):
        return len(self.cards)

    def get(self, card_number):
        """Returns the card with the given number"""
        assert isinstance(card_number, int)
        card = self.cards[card_number]
        if not card:
            raise ValueError("Invalid card number %d" % card_number)
        return card
