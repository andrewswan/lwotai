from lwotai.cards.card import Card
from lwotai.cards.card1 import Card1
from lwotai.cards.card2 import Card2
from lwotai.cards.card3 import Card3
from lwotai.cards.card4 import Card4
from lwotai.cards.card5 import Card5
from lwotai.cards.card6_7 import Card6and7
from lwotai.cards.card8_9_10 import Card8and9and10
from lwotai.cards.card11 import Card11
from lwotai.cards.card12 import Card12
from lwotai.cards.card13 import Card13
from lwotai.cards.card14 import Card14
from lwotai.cards.card15 import Card15

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
    Card(16, "US", "Euro-Islam", 2, True, False, False),
    Card(17, "US", "FSB", 2, False, False, False),
    Card(18, "US", "Intel Community", 2, False, False, False),
    Card(19, "US", "Kemalist Republic", 2, False, False, False),
    Card(20, "US", "King Abdullah", 2, True, False, False),
    Card(21, "US", "Let's Roll", 2, False, False, False),
    Card(22, "US", "Mossad and Shin Bet", 2, False, False, False),
    Card(23, "US", "Predator", 2, False, False, False),
    Card(24, "US", "Predator", 2, False, False, False),
    Card(25, "US", "Predator", 2, False, False, False),
    Card(26, "US", "Quartet", 2, False, False, False),
    Card(27, "US", "Saddam Captured", 2, True, True, False),
    Card(28, "US", "Sharia", 2, False, False, False),
    Card(29, "US", "Tony Blair", 2, True, False, False),
    Card(30, "US", "UN Nation Building", 2, False, False, False),
    Card(31, "US", "Wiretapping", 2, False, True, False),
    Card(32, "US", "Back Channel", 3, False, False, False),
    Card(33, "US", "Benazir Bhutto", 3, True, True, False),
    Card(34, "US", "Enhanced Measures", 3, False, True, False),
    Card(35, "US", "Hijab", 3, True, False, False),
    Card(36, "US", "Indo-Pakistani Talks", 3, True, True, False),
    Card(37, "US", "Iraqi WMD", 3, True, True, False),
    Card(38, "US", "Libyan Deal", 3, True, True, False),
    Card(39, "US", "Libyan WMD", 3, True, True, False),
    Card(40, "US", "Mass Turnout", 3, False, False, False),
    Card(41, "US", "NATO", 3, False, True, False),
    Card(42, "US", "Pakistani Offensive", 3, False, False, False),
    Card(43, "US", "Patriot Act", 3, True, True, False),
    Card(44, "US", "Renditions", 3, False, True, False),
    Card(45, "US", "Safer Now", 3, False, False, False),
    Card(46, "US", "Sistani", 3, False, False, False),
    Card(47, "US", "The door of Itjihad was closed", 3, False, False, True),
    Card(48, "Jihadist", "Adam Gadahn", 1, False, False, False),
    Card(49, "Jihadist", "Al-Ittihad al-Islami", 1, True, False, False),
    Card(50, "Jihadist", "Ansar al-Islam", 1, True, False, False),
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