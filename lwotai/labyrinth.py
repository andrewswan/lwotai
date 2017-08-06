import random

from card import Card
from country import Country
from governance import GOOD, FAIR, POOR
from governance import governance_with_level
from randomizer import Randomizer
from saver import Saver
from ideologies.ideology import get_ideology, IDEOLOGIES
from scenarios.scenario import get_scenario
from utils import Utils


class Labyrinth:
    """The main game entity"""

    def __init__(self, scenario_num, ideology_num, setup_function=None, test_user_input=None, **kwargs):
        # Inputs
        self.scenario = get_scenario(scenario_num)
        self.ideology = get_ideology(ideology_num)
        self.testUserInput = test_user_input
        self.randomizer = kwargs.get('randomizer', Randomizer())
        self.saver = kwargs.get('saver', Saver())
        # Defaults
        self.backlashInPlay = False
        self.cells = 0
        self.deck = {}
        self.funding = 0
        self.gameOver = False
        self.history = []
        self.lapsing = []
        self.map = {}
        self.markers = []
        self.phase = ""
        self.prestige = 0
        self.prompt = "Command: "
        self.roll_turn = -1
        self.startYear = 0
        self.troops = 0
        self.turn = 1
        self.uCard = 1
        self.undo = False
        self.validCountryMarkers = []
        self.validGlobalMarkers = []
        self.validLapsingMarkers = []
        self.whichPlayer= ""
        # Initialise
        self.deckSetup()
        self.mapSetup()
        self.validMarkersSetup()
        # Apply any passed-in setup function
        if setup_function:
            setup_function(self)
        else:
            self.scenario.set_up(self)
            self._print_initial_state()
        self._print_game_start_messages()

    def _print_game_start_messages(self):
        self.outputToHistory(self.scenario.name, False)
        self.outputToHistory("Jihadist Ideology: " + self.ideology.name, False)
        print ""
        self.outputToHistory("Game Start")
        self.outputToHistory("")
        self.outputToHistory("[[ %d (Turn %s) ]]" % (self.startYear + (self.turn - 1), self.turn), True)

    def debugPrint(self, str):
        return

    def outputToHistory(self, output, lineFeed=True):
        print output
        self.history.append(output)
        if lineFeed:
            print ""

    def mapSetup(self):
        self.map["Canada"] = Country(self, "Canada", "Non-Muslim", "", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["United States"] = Country(self, "United States", "Non-Muslim", "Hard", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["United Kingdom"] = Country(self, "United Kingdom", "Non-Muslim", "", GOOD, False, 3, 0, 0, 0, False, 0)
        self.map["Serbia"] = Country(self, "Serbia", "Non-Muslim", "", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["Israel"] = Country(self, "Israel", "Non-Muslim", "Hard", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["India"] = Country(self, "India", "Non-Muslim", "", GOOD, False, 0, 0, 0, 0, False, 0)
        self.map["Scandinavia"] = Country(self, "Scandinavia", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Eastern Europe"] = Country(self, "Eastern Europe", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Benelux"] = Country(self, "Benelux", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Germany"] = Country(self, "Germany", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["France"] = Country(self, "France", "Non-Muslim", "", GOOD, True, 2, 0, 0, 0, False, 0)
        self.map["Italy"] = Country(self, "Italy", "Non-Muslim", "", GOOD, True, 0, 0, 0, 0, False, 0)
        self.map["Spain"] = Country(self, "Spain", "Non-Muslim", "", GOOD, True, 2, 0, 0, 0, False, 0)
        self.map["Russia"] = Country(self, "Russia", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Caucasus"] = Country(self, "Caucasus", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["China"] = Country(self, "China", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Kenya/Tanzania"] = Country(self, "Kenya/Tanzania", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Thailand"] = Country(self, "Thailand", "Non-Muslim", "", FAIR, False, 0, 0, 0, 0, False, 0)
        self.map["Philippines"] = Country(self, "Philippines", "Non-Muslim", "", FAIR, False, 3, 0, 0, 0, False, 0)
        self.map["Morocco"] = Country(self, "Morocco", "Suni", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Algeria/Tunisia"] = Country(self, "Algeria/Tunisia", "Suni", "", None, False, 0, 0, 0, 0, True, 2)
        self.map["Libya"] = Country(self, "Libya", "Suni", "", None, False, 0, 0, 0, 0, True, 1)
        self.map["Egypt"] = Country(self, "Egypt", "Suni", "", None, False, 0, 0, 0, 0, False, 3)
        self.map["Sudan"] = Country(self, "Sudan", "Suni", "", None, False, 0, 0, 0, 0, True, 1)
        self.map["Somalia"] = Country(self, "Somalia", "Suni", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Jordan"] = Country(self, "Jordan", "Suni", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Syria"] = Country(self, "Syria", "Suni", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Central Asia"] = Country(self, "Central Asia", "Suni", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Indonesia/Malaysia"] = Country(self, "Indonesia/Malaysia", "Suni", "", None, False, 0, 0, 0, 0, True, 3)
        self.map["Turkey"] = Country(self, "Turkey", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Lebanon"] = Country(self, "Lebanon", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Yemen"] = Country(self, "Yemen", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Iraq"] = Country(self, "Iraq", "Shia-Mix", "", None, False, 0, 0, 0, 0, True, 3)
        self.map["Saudi Arabia"] = Country(self, "Saudi Arabia", "Shia-Mix", "", None, False, 0, 2, 0, 0, True, 3)
        self.map["Gulf States"] = Country(self, "Gulf States", "Shia-Mix", "", None, False, 0, 2, 0, 0, True, 3)
        self.map["Pakistan"] = Country(self, "Pakistan", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 2)
        self.map["Afghanistan"] = Country(self, "Afghanistan", "Shia-Mix", "", None, False, 0, 0, 0, 0, False, 1)
        self.map["Iran"] = Country(self, "Iran", "Iran", None, FAIR, False, 0, 0, 0, 0, False, 0)

        # Canada
        self.map["Canada"].links.append(self.map["United States"])
        self.map["Canada"].links.append(self.map["United Kingdom"])
        self.map["Canada"].schengenLink = True
        # United States
        self.map["United States"].links.append(self.map["Canada"])
        self.map["United States"].links.append(self.map["United Kingdom"])
        self.map["United States"].links.append(self.map["Philippines"])
        self.map["United States"].schengenLink = True
        # United Kingdom
        self.map["United Kingdom"].links.append(self.map["Canada"])
        self.map["United Kingdom"].links.append(self.map["United States"])
        self.map["United Kingdom"].schengenLink = True
        # Serbia
        self.map["Serbia"].links.append(self.map["Russia"])
        self.map["Serbia"].links.append(self.map["Turkey"])
        self.map["Serbia"].schengenLink = True
        # Israel
        self.map["Israel"].links.append(self.map["Lebanon"])
        self.map["Israel"].links.append(self.map["Jordan"])
        self.map["Israel"].links.append(self.map["Egypt"])
        # India
        self.map["India"].links.append(self.map["Pakistan"])
        self.map["India"].links.append(self.map["Indonesia/Malaysia"])
        # Russia
        self.map["Russia"].links.append(self.map["Serbia"])
        self.map["Russia"].links.append(self.map["Turkey"])
        self.map["Russia"].links.append(self.map["Caucasus"])
        self.map["Russia"].links.append(self.map["Central Asia"])
        self.map["Russia"].schengenLink = True
        # Caucasus
        self.map["Caucasus"].links.append(self.map["Russia"])
        self.map["Caucasus"].links.append(self.map["Turkey"])
        self.map["Caucasus"].links.append(self.map["Iran"])
        self.map["Caucasus"].links.append(self.map["Central Asia"])
        # China
        self.map["China"].links.append(self.map["Central Asia"])
        self.map["China"].links.append(self.map["Thailand"])
        # Kenya/Tanzania
        self.map["Kenya/Tanzania"].links.append(self.map["Sudan"])
        self.map["Kenya/Tanzania"].links.append(self.map["Somalia"])
        # Thailand
        self.map["Thailand"].links.append(self.map["China"])
        self.map["Thailand"].links.append(self.map["Philippines"])
        self.map["Thailand"].links.append(self.map["Indonesia/Malaysia"])
        # Philippines
        self.map["Philippines"].links.append(self.map["United States"])
        self.map["Philippines"].links.append(self.map["Thailand"])
        self.map["Philippines"].links.append(self.map["Indonesia/Malaysia"])
        # Morocco
        self.map["Morocco"].links.append(self.map["Algeria/Tunisia"])
        self.map["Morocco"].schengenLink = True
        # Algeria/Tunisia
        self.map["Algeria/Tunisia"].links.append(self.map["Morocco"])
        self.map["Algeria/Tunisia"].links.append(self.map["Libya"])
        self.map["Algeria/Tunisia"].schengenLink = True
        # Libya
        self.map["Libya"].links.append(self.map["Algeria/Tunisia"])
        self.map["Libya"].links.append(self.map["Egypt"])
        self.map["Libya"].links.append(self.map["Sudan"])
        self.map["Libya"].schengenLink = True
        # Egypt
        self.map["Egypt"].links.append(self.map["Libya"])
        self.map["Egypt"].links.append(self.map["Israel"])
        self.map["Egypt"].links.append(self.map["Sudan"])
        # Sudan
        self.map["Sudan"].links.append(self.map["Libya"])
        self.map["Sudan"].links.append(self.map["Egypt"])
        self.map["Sudan"].links.append(self.map["Kenya/Tanzania"])
        self.map["Sudan"].links.append(self.map["Somalia"])
        # Somalia
        self.map["Somalia"].links.append(self.map["Sudan"])
        self.map["Somalia"].links.append(self.map["Kenya/Tanzania"])
        self.map["Somalia"].links.append(self.map["Yemen"])
        # Jordan
        self.map["Jordan"].links.append(self.map["Israel"])
        self.map["Jordan"].links.append(self.map["Syria"])
        self.map["Jordan"].links.append(self.map["Iraq"])
        self.map["Jordan"].links.append(self.map["Saudi Arabia"])
        # Syria
        self.map["Syria"].links.append(self.map["Turkey"])
        self.map["Syria"].links.append(self.map["Lebanon"])
        self.map["Syria"].links.append(self.map["Jordan"])
        self.map["Syria"].links.append(self.map["Iraq"])
        # Central Asia
        self.map["Central Asia"].links.append(self.map["Russia"])
        self.map["Central Asia"].links.append(self.map["Caucasus"])
        self.map["Central Asia"].links.append(self.map["Iran"])
        self.map["Central Asia"].links.append(self.map["Afghanistan"])
        self.map["Central Asia"].links.append(self.map["China"])
        # Indonesia/Malaysia
        self.map["Indonesia/Malaysia"].links.append(self.map["Thailand"])
        self.map["Indonesia/Malaysia"].links.append(self.map["India"])
        self.map["Indonesia/Malaysia"].links.append(self.map["Philippines"])
        self.map["Indonesia/Malaysia"].links.append(self.map["Pakistan"])
        # Turkey
        self.map["Turkey"].links.append(self.map["Serbia"])
        self.map["Turkey"].links.append(self.map["Russia"])
        self.map["Turkey"].links.append(self.map["Caucasus"])
        self.map["Turkey"].links.append(self.map["Iran"])
        self.map["Turkey"].links.append(self.map["Syria"])
        self.map["Turkey"].links.append(self.map["Iraq"])
        self.map["Turkey"].schengenLink = True
        # Lebanon
        self.map["Lebanon"].links.append(self.map["Syria"])
        self.map["Lebanon"].links.append(self.map["Israel"])
        self.map["Lebanon"].schengenLink = True
        # Yemen
        self.map["Yemen"].links.append(self.map["Saudi Arabia"])
        self.map["Yemen"].links.append(self.map["Somalia"])
        # Iraq
        self.map["Iraq"].links.append(self.map["Syria"])
        self.map["Iraq"].links.append(self.map["Turkey"])
        self.map["Iraq"].links.append(self.map["Iran"])
        self.map["Iraq"].links.append(self.map["Gulf States"])
        self.map["Iraq"].links.append(self.map["Saudi Arabia"])
        self.map["Iraq"].links.append(self.map["Jordan"])
        # Saudi Arabia
        self.map["Saudi Arabia"].links.append(self.map["Jordan"])
        self.map["Saudi Arabia"].links.append(self.map["Iraq"])
        self.map["Saudi Arabia"].links.append(self.map["Gulf States"])
        self.map["Saudi Arabia"].links.append(self.map["Yemen"])
        # Gulf States
        self.map["Gulf States"].links.append(self.map["Iran"])
        self.map["Gulf States"].links.append(self.map["Pakistan"])
        self.map["Gulf States"].links.append(self.map["Saudi Arabia"])
        self.map["Gulf States"].links.append(self.map["Iraq"])
        # Pakistan
        self.map["Pakistan"].links.append(self.map["Iran"])
        self.map["Pakistan"].links.append(self.map["Afghanistan"])
        self.map["Pakistan"].links.append(self.map["India"])
        self.map["Pakistan"].links.append(self.map["Gulf States"])
        self.map["Pakistan"].links.append(self.map["Indonesia/Malaysia"])
        # Afghanistan
        self.map["Afghanistan"].links.append(self.map["Central Asia"])
        self.map["Afghanistan"].links.append(self.map["Pakistan"])
        self.map["Afghanistan"].links.append(self.map["Iran"])
        # Iran
        self.map["Iran"].links.append(self.map["Central Asia"])
        self.map["Iran"].links.append(self.map["Afghanistan"])
        self.map["Iran"].links.append(self.map["Pakistan"])
        self.map["Iran"].links.append(self.map["Gulf States"])
        self.map["Iran"].links.append(self.map["Iraq"])
        self.map["Iran"].links.append(self.map["Turkey"])
        self.map["Iran"].links.append(self.map["Caucasus"])

    def _print_initial_state(self):
        """Performs any setup necessary after the scenario-specific setup"""
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
            elif self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        print "Good Resources:     %d" % goodRes
        print "Islamist Resources: %d" % islamRes
        print "---"
        print "Good/Fair Countries:     %d" % goodC
        print "Poor/Islamist Countries: %d" % islamC
        print ""
        print "GWOT"
        print "US Posture: %s" % self.map["United States"].posture
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        print "World Posture: %s %d" % (worldPosStr, abs(worldPos))
        print "US Prestige: %d" % self.prestige
        print ""

    def deckSetup(self):
        self.deck["1"] = Card(1,"US","Backlash", 1, False, False, False)
        self.deck["2"] = Card(2,"US","Biometrics", 1, False, False, True)
        self.deck["3"] = Card(3,"US","CTR", 1, False, True, False)
        self.deck["4"] = Card(4,"US","Moro Talks", 1, True, True, False)
        self.deck["5"] = Card(5,"US","NEST", 1, True, True, False)
        self.deck["6"] = Card(6,"US","Sanctions", 1, False, False, False)
        self.deck["7"] = Card(7,"US","Sanctions", 1, False, False, False)
        self.deck["8"] = Card(8,"US","Special Forces", 1, False, False, False)
        self.deck["9"] = Card(9,"US","Special Forces", 1, False, False, False)
        self.deck["10"] = Card(10,"US","Special Forces", 1, False, False, False)
        self.deck["11"] = Card(11,"US","Abbas", 2, True, True, False)
        self.deck["12"] = Card(12,"US","Al-Azhar", 2, False, False, False)
        self.deck["13"] = Card(13,"US","Anbar Awakening", 2, False, True, False)
        self.deck["14"] = Card(14,"US","Covert Action", 2, False, False, False)
        self.deck["15"] = Card(15,"US","Ethiopia Strikes", 2, True, False, False)
        self.deck["16"] = Card(16,"US","Euro-Islam", 2, True, False, False)
        self.deck["17"] = Card(17,"US","FSB", 2, False, False, False)
        self.deck["18"] = Card(18,"US","Intel Community", 2, False, False, False)
        self.deck["19"] = Card(19,"US","Kemalist Republic", 2, False, False, False)
        self.deck["20"] = Card(20,"US","King Abdullah", 2, True, False, False)
        self.deck["21"] = Card(21,"US","Let's Roll", 2, False, False, False)
        self.deck["22"] = Card(22,"US","Mossad and Shin Bet", 2, False, False, False)
        self.deck["23"] = Card(23,"US","Predator", 2, False, False, False)
        self.deck["24"] = Card(24,"US","Predator", 2, False, False, False)
        self.deck["25"] = Card(25,"US","Predator", 2, False, False, False)
        self.deck["26"] = Card(26,"US","Quartet", 2, False, False, False)
        self.deck["27"] = Card(27,"US","Sadam Captured", 2, True, True, False)
        self.deck["28"] = Card(28,"US","Sharia", 2, False, False, False)
        self.deck["29"] = Card(29,"US","Tony Blair", 2, True, False, False)
        self.deck["30"] = Card(30,"US","UN Nation Building", 2, False, False, False)
        self.deck["31"] = Card(31,"US","Wiretapping", 2, False, True, False)
        self.deck["32"] = Card(32,"US","Back Channel", 3, False, False, False)
        self.deck["33"] = Card(33,"US","Benazir Bhutto", 3, True, True, False)
        self.deck["34"] = Card(34,"US","Enhanced Measures", 3, False, True, False)
        self.deck["35"] = Card(35,"US","Hijab", 3, True, False, False)
        self.deck["36"] = Card(36,"US","Indo-Pakistani Talks", 3, True, True, False)
        self.deck["37"] = Card(37,"US","Iraqi WMD", 3, True, True, False)
        self.deck["38"] = Card(38,"US","Libyan Deal", 3, True, True, False)
        self.deck["39"] = Card(39,"US","Libyan WMD", 3, True, True, False)
        self.deck["40"] = Card(40,"US","Mass Turnout", 3, False, False, False)
        self.deck["41"] = Card(41,"US","NATO", 3, False, True, False)
        self.deck["42"] = Card(42,"US","Pakistani Offensive", 3, False, False, False)
        self.deck["43"] = Card(43,"US","Patriot Act", 3, True, True, False)
        self.deck["44"] = Card(44,"US","Renditions", 3, False, True, False)
        self.deck["45"] = Card(45,"US","Safer Now", 3, False, False, False)
        self.deck["46"] = Card(46,"US","Sistani", 3, False, False, False)
        self.deck["47"] = Card(47,"US","The door of Itjihad was closed", 3, False, False, True)
        self.deck["48"] = Card(48,"Jihadist","Adam Gadahn", 1, False, False, False)
        self.deck["49"] = Card(49,"Jihadist","Al-Ittihad al-Islami", 1, True, False, False)
        self.deck["50"] = Card(50,"Jihadist","Ansar al-Islam", 1, True, False, False)
        self.deck["51"] = Card(51,"Jihadist","FREs", 1, False, False, False)
        self.deck["52"] = Card(52,"Jihadist","IEDs", 1, False, False, False)
        self.deck["53"] = Card(53,"Jihadist","Madrassas", 1, False, False, False)
        self.deck["54"] = Card(54,"Jihadist","Moqtada al-Sadr", 1, True, True, False)
        self.deck["55"] = Card(55,"Jihadist","Uyghur Jihad", 1, True, False, False)
        self.deck["56"] = Card(56,"Jihadist","Vieira de Mello Slain", 1, True, True, False)
        self.deck["57"] = Card(57,"Jihadist","Abu Sayyaf", 2, True, True, False)
        self.deck["58"] = Card(58,"Jihadist","Al-Anbar", 2, True, True, False)
        self.deck["59"] = Card(59,"Jihadist","Amerithrax", 2, False, False, False)
        self.deck["60"] = Card(60,"Jihadist","Bhutto Shot", 2, True, True, False)
        self.deck["61"] = Card(61,"Jihadist","Detainee Release", 2, False, False, False)
        self.deck["62"] = Card(62,"Jihadist","Ex-KGB", 2, False, False, False)
        self.deck["63"] = Card(63,"Jihadist","Gaza War", 2, False, False, False)
        self.deck["64"] = Card(64,"Jihadist","Hariri Killed", 2, True, False, False)
        self.deck["65"] = Card(65,"Jihadist","HEU", 2, True, False, False)
        self.deck["66"] = Card(66,"Jihadist","Homegrown", 2, False, False, False)
        self.deck["67"] = Card(67,"Jihadist","Islamic Jihad Union", 2, True, False, False)
        self.deck["68"] = Card(68,"Jihadist","Jemaah Islamiya", 2, False, False, False)
        self.deck["69"] = Card(69,"Jihadist","Kazakh Strain", 2, True, False, False)
        self.deck["70"] = Card(70,"Jihadist","Lashkar-e-Tayyiba", 2, False, False, False)
        self.deck["71"] = Card(71,"Jihadist","Loose Nuke", 2, True, False, False)
        self.deck["72"] = Card(72,"Jihadist","Opium", 2, False, False, False)
        self.deck["73"] = Card(73,"Jihadist","Pirates", 2, True, True, False)
        self.deck["74"] = Card(74,"Jihadist","Schengen Visas", 2, False, False, False)
        self.deck["75"] = Card(75,"Jihadist","Schroeder & Chirac", 2, True, False, False)
        self.deck["76"] = Card(76,"Jihadist","Abu Ghurayb", 3, True, False, False)
        self.deck["77"] = Card(77,"Jihadist","Al Jazeera", 3, False, False, False)
        self.deck["78"] = Card(78,"Jihadist","Axis of Evil", 3, False, False, False)
        self.deck["79"] = Card(79,"Jihadist","Clean Operatives", 3, False, False, False)
        self.deck["80"] = Card(80,"Jihadist","FATA", 3, False, True, False)
        self.deck["81"] = Card(81,"Jihadist","Foreign Fighters", 3, False, False, False)
        self.deck["82"] = Card(82,"Jihadist","Jihadist Videos", 3, False, False, False)
        self.deck["83"] = Card(83,"Jihadist","Kashmir", 3, False, False, False)
        self.deck["84"] = Card(84,"Jihadist","Leak", 3, False, False, False)
        self.deck["85"] = Card(85,"Jihadist","Leak", 3, False, False, False)
        self.deck["86"] = Card(86,"Jihadist","Lebanon War", 3, False, False, False)
        self.deck["87"] = Card(87,"Jihadist","Martyrdom Operation", 3, False, False, False)
        self.deck["88"] = Card(88,"Jihadist","Martyrdom Operation", 3, False, False, False)
        self.deck["89"] = Card(89,"Jihadist","Martyrdom Operation", 3, False, False, False)
        self.deck["90"] = Card(90,"Jihadist","Quagmire", 3, False, False, False)
        self.deck["91"] = Card(91,"Jihadist","Regional al-Qaeda", 3, False, False, False)
        self.deck["92"] = Card(92,"Jihadist","Saddam", 3, False, False, False)
        self.deck["93"] = Card(93,"Jihadist","Taliban", 3, False, False, False)
        self.deck["94"] = Card(94,"Jihadist","The door of Itjihad was closed", 3, False, False, False)
        self.deck["95"] = Card(95,"Jihadist","Wahhabism", 3, False, False, False)
        self.deck["96"] = Card(96,"Unassociated","Danish Cartoons", 1, True, False, False)
        self.deck["97"] = Card(97,"Unassociated","Fatwa", 1, False, False, False)
        self.deck["98"] = Card(98,"Unassociated","Gaza Withdrawal", 1, True, False, False)
        self.deck["99"] = Card(99,"Unassociated","HAMAS Elected", 1, True, False, False)
        self.deck["100"] = Card(100,"Unassociated","Hizb Ut-Tahrir", 1, False, False, False)
        self.deck["101"] = Card(101,"Unassociated","Kosovo", 1, False, False, False)
        self.deck["102"] = Card(102,"Unassociated","Former Soviet Union", 2, False, False, False)
        self.deck["103"] = Card(103,"Unassociated","Hizballah", 2, False, False, False)
        self.deck["104"] = Card(104,"Unassociated","Iran", 2, False, False, False)
        self.deck["105"] = Card(105,"Unassociated","Iran", 2, False, False, False)
        self.deck["106"] = Card(106,"Unassociated","Jaysh al-Mahdi", 2, False, False, False)
        self.deck["107"] = Card(107,"Unassociated","Kurdistan", 2, False, False, False)
        self.deck["108"] = Card(108,"Unassociated","Musharraf", 2, False, False, False)
        self.deck["109"] = Card(109,"Unassociated","Tora Bora", 2, True, False, False)
        self.deck["110"] = Card(110,"Unassociated","Zarqawi", 2, False, False, False)
        self.deck["111"] = Card(111,"Unassociated","Zawahiri", 2, False, False, False)
        self.deck["112"] = Card(112,"Unassociated","Bin Ladin", 3, False, False, False)
        self.deck["113"] = Card(113,"Unassociated","Darfur", 3, False, False, False)
        self.deck["114"] = Card(114,"Unassociated","GTMO", 3, False, False, True)
        self.deck["115"] = Card(115,"Unassociated","Hambali", 3, False, False, False)
        self.deck["116"] = Card(116,"Unassociated","KSM", 3, False, False, False)
        self.deck["117"] = Card(117,"Unassociated","Oil Price Spike", 3, False, False, True)
        self.deck["118"] = Card(118,"Unassociated","Oil Price Spike", 3, False, False, True)
        self.deck["119"] = Card(119,"Unassociated","Saleh", 3, False, False, False)
        self.deck["120"] = Card(120,"Unassociated","US Election", 3, False, False, False)

    # 20150131PS Start

    def validMarkersSetup(self):
        self.validGlobalMarkers.append("Moro Talks")
        self.validGlobalMarkers.append("NEST")
        self.validGlobalMarkers.append("Abbas")
        self.validGlobalMarkers.append("Anbar Awakening")
        self.validGlobalMarkers.append("Saddam Captured")
        self.validGlobalMarkers.append("Wiretapping")
        self.validGlobalMarkers.append("Benazir Bhutto")
        self.validGlobalMarkers.append("Enhanced Measures")
        self.validGlobalMarkers.append("Indo-Pakistani Talks")
        self.validGlobalMarkers.append("Iraqi WMD")
        self.validGlobalMarkers.append("Libyan Deal")
        self.validGlobalMarkers.append("Libyan WMD")
        self.validGlobalMarkers.append("Patriot Act")
        self.validGlobalMarkers.append("Renditions")
        self.validGlobalMarkers.append("Vieira de Mello Slain")
        self.validGlobalMarkers.append("Abu Sayyaf")
        self.validGlobalMarkers.append("Al-Anbar")
        self.validGlobalMarkers.append("Bhutto Shot")
        self.validGlobalMarkers.append("Pirates")
        self.validGlobalMarkers.append("Leak-Enhanced Measures")
        self.validGlobalMarkers.append("Leak-Wiretapping")
        self.validGlobalMarkers.append("Leak-Renditions")
        self.validCountryMarkers.append("CTR")    # 20150616PS
        self.validCountryMarkers.append("NATO")
        self.validCountryMarkers.append("Sadr")
        self.validCountryMarkers.append("FATA")
        self.validLapsingMarkers.append("Biometrics")
        self.validLapsingMarkers.append("The door of Itjihad was closed")
        self.validLapsingMarkers.append("GTMO")
        self.validLapsingMarkers.append("Oil Price Spike")

    def my_raw_input(self, prompt):
        """Reads a line from the test input, if any is left, otherwise from standard input"""
        fake_input = self._next_fake_user_input()
        if fake_input:
            print "TEST: Prompt: '%s' Value: '%s'" % (prompt, fake_input)
            return fake_input
        return raw_input(prompt)

    def _next_fake_user_input(self):
        """Returns the next line of fake user input, or None"""
        if self.testUserInput and len(self.testUserInput) > 0:
            return self.testUserInput.pop(0)
        return None

    def getCountryFromUser(self, prompt, special, helpFunction, helpParameter = None):
        goodCountry = None
        while not goodCountry:
            input = self.my_raw_input(prompt)
            if input == "":
                return ""
            elif input == "?" and helpFunction:
                helpFunction(helpParameter)
                continue
            elif input == special:
                return special
            possible = []
            for country in self.map:
                if input.lower() == country.lower():
                    possible = [country]
                    break
                elif input.lower() in country.lower():
                    possible.append(country)
            if len(possible) == 0:
                print "Unrecognized country."
                print ""
            elif len(possible) > 1:
                print "Be more specific", possible
                print ""
            else:
                goodCountry = possible[0]
        return goodCountry

    def getNumTroopsFromUser(self, prompt, max):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                input = int(input)
                if input <= max:
                    return input
                else:
                    print "Not enough troops."
                    print ""
            except:
                print "Entry error"
                print ""

    def getCardNumFromUser(self, prompt):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "none":
                    return "none"
                input = int(input)
                if input <= 120:
                    return input
                else:
                    print "Enter a card number."
                    print ""
            except:
                print "Enter a card number."
                print ""

    def getPlotTypeFromUser(self, prompt):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "w" or input.lower() == "wmd":
                    return "WMD"
                input = int(input)
                if 1 <= input <= 3:
                    return input
                else:
                    print "Enter 1, 2, 3 or W for WMD."
                    print ""
            except:
                print "Enter 1, 2, 3 or W for WMD."
                print ""

    def getRollFromUser(self, prompt):
        goodNum = None
        while not goodNum:
            try:
                input = self.my_raw_input(prompt)
                if input == "r":
                    roll = random.randint(1, 6)
                    print "Roll: %d" % roll
                    return roll
                input = int(input)
                if 1 <= input <= 6:
                    return input
                else:
                    raise
            except:
                print "Entry error"
                print ""

    def getYesNoFromUser(self, prompt):
        good = None
        while not good:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "y" or input.lower() == "yes":
                    return True
                elif input.lower() == "n" or input.lower() == "no":
                    return False
                else:
                    print "Enter y or n."
                    print ""
            except:
                print "Enter y or n."
                print ""

    def getPostureFromUser(self, prompt):
        good = None
        while not good:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "h" or input.lower() == "hard":
                    return "Hard"
                elif input.lower() == "s" or input.lower() == "soft":
                    return "Soft"
                else:
                    print "Enter h or s."
                    print ""
            except:
                print "Enter h or s."
                print ""

    def getEventOrOpsFromUser(self, prompt):
        good = None
        while not good:
            try:
                input = self.my_raw_input(prompt)
                if input.lower() == "e" or input.lower() == "event":
                    return "event"
                elif input.lower() == "o" or input.lower() == "ops":
                    return "ops"
                else:
                    print "Enter e or o."
                    print ""
            except:
                print "Enter e or o."
                print ""

    def modifiedWoIRoll(self, baseRoll, country, useGWOTPenalty = True):
        modRoll = baseRoll

        if self.prestige <= 3:
            modRoll -= 1
            self.outputToHistory("-1 for Prestige", False)
        elif self.prestige >= 7 and self.prestige <= 9:
            modRoll += 1
            self.outputToHistory("+1 for Prestige", False)
        elif self.prestige >= 10:
            modRoll += 2
            self.outputToHistory("+2 for Prestige", False)

        if self.map[country].is_ally() and self.map[country].is_fair():
            modRoll -= 1
            self.outputToHistory("-1 for Attempt to shift to Good", False)

        if useGWOTPenalty:
            modRoll += self.gwotPenalty()
            if self.gwotPenalty() <> 0:
                self.outputToHistory("-1 for GWOT Relations Penalty", False)

        if self.map[country].aid > 0:
            modRoll += self.map[country].aid    # 20150131PS use number of aid markers rather than 1
            self.outputToHistory("+%s for Aid" % self.map[country].aid, False)

        for adj in self.map[country].links:
            if adj.is_ally() and adj.is_good():
                modRoll += 1
                self.outputToHistory("+1 for Adjacent Good Ally", False)
                break
        return modRoll

    def gwotPenalty(self):
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        if worldPos > 3:
            worldPos = 3
        elif worldPos < -3:
            worldPos = -3
        if self.map["United States"].posture != worldPosStr:
            return -(abs(worldPos))
        else:
            return 0

    def changePrestige(self, delta, lineFeed=True):
        """Changes US prestige by the given amount, then prints the new value"""
        if delta < 0:
            self._reduce_prestige(-delta)
        elif delta > 0:
            self._increase_prestige(delta)
        self.outputToHistory("Prestige now %d" % self.prestige, lineFeed)

    def changeFunding(self, delta, lineFeed=True):
        self.funding += delta
        if self.funding < 1:
            self.funding = 1
        elif self.funding > 9:
            self.funding = 9
        self.outputToHistory("Jihadist Funding now %d" % self.funding, lineFeed)

    def validate(self):
        """Checks that this instance is in a valid state"""
        # Check cells
        cellCount = 0
        for country_name in self.map:
            country = self.map[country_name]
            cellCount += country.activeCells + country.sleeperCells
        cellCount += self.cells
        assert cellCount == 15, "Expected 15 cells but have %d" % cellCount
        # Check troops
        troopCount = 0
        for country in self.map:
            troopCount += self.map[country].troops()
        troopCount += self.troops
        assert troopCount == 15, "Expected 15 troops but have %d" % troopCount
        # Check tested countries
        for country_name in self.map:
            self.map[country_name].check_is_tested()

    def placeCells(self, country, numCells):
        if self.cells == 0:
            self.outputToHistory("No cells are on the Funding Track.", True)
        else:
            self.testCountry(country)
            cellsToMove = min(numCells, self.cells)
            self.map[country].sleeperCells += cellsToMove
            # remove cadre
            self.map[country].cadre = 0
            self.cells -= cellsToMove
            self.outputToHistory("%d Sleeper Cell(s) placed in %s" % (cellsToMove, country), False)
            self.outputToHistory(self.map[country].countryStr(), True)

    def removeCell(self, country, side):
        # 20150131PS included Sadr in cell count, added test for side to determine order of removal
        if self.map[country].totalCells(True) == 0:
            return
        if side == "US":
            if self.map[country].sleeperCells > 0:
                self.map[country].sleeperCells -= 1
                self.cells += 1
                self.outputToHistory("Sleeper Cell removed from %s." % country, True)
            elif "Sadr" in self.map[country].markers:
                self.map[country].markers.remove("Sadr")
                self.outputToHistory("Sadr removed from %s." % country, True)
            elif self.map[country].activeCells > 0:
                self.map[country].activeCells -= 1
                self.cells += 1
                self.outputToHistory("Active Cell removed from %s." % country, True)
        else:
            if self.map[country].activeCells > 0:
                self.map[country].activeCells -= 1
                self.cells += 1
                self.outputToHistory("Active Cell removed from %s." % country, True)
            elif self.map[country].sleeperCells > 0:
                self.map[country].sleeperCells -= 1
                self.cells += 1
                self.outputToHistory("Sleeper Cell removed from %s." % country, True)
            elif "Sadr" in self.map[country].markers:
                self.map[country].markers.remove("Sadr")
                self.outputToHistory("Sadr removed from %s." % country, True)
        if self.map[country].totalCells() == 0:
            self.outputToHistory("Cadre added in %s." % country, True)
            self.map[country].cadre = 1

    def removeAllCellsFromCountry(self, country):
        cellsToRemove = self.map[country].totalCells()
        if self.map[country].sleeperCells > 0:
            numCells = self.map[country].sleeperCells
            self.map[country].sleeperCells -= numCells
            self.cells += numCells
            self.outputToHistory("%d Sleeper Cell(s) removed from %s." % (numCells, country), False)
        if self.map[country].activeCells > 0:
            numCells = self.map[country].activeCells
            self.map[country].activeCells -= numCells
            self.cells += numCells
            self.outputToHistory("%d Active Cell(s) removed from %s." % (numCells, country), False)
        if cellsToRemove > 0:
            self.outputToHistory("Cadre added in %s." % country, False)
            self.map[country].cadre = 1

    def improveGovernance(self, country):
        self.map[country].improve_governance()

    def worsenGovernance(self, country):
        self.map[country].worsenGovernance()

    def numCellsAvailable(self, ignoreFunding=False):

        retVal = self.cells
        if ignoreFunding:
            return retVal

        if self.funding <= 3:
            retVal -= 10
        elif self.funding <= 6:
            retVal -= 5
        return max(retVal, 0)

    def numIslamistRule(self):
        numIR = 0
        for country in self.map:
            if self.map[country].is_islamist_rule():
                numIR += 1
        return numIR

    def numBesieged(self):
        numBesieged = 0
        for country in self.map:
            if self.map[country].besieged > 0:
                numBesieged += 1
        return numBesieged

    def numRegimeChange(self):
        numRC = 0
        for country in self.map:
            if self.map[country].regimeChange > 0:
                numRC += 1
        return numRC

    def numAdversary(self):
        numAdv = 0
        for country in self.map:
            if self.map[country].is_adversary():
                numAdv += 1
        return numAdv

    def num_disruptable(self):
        """Returns the number of countries in which the US player can Disrupt"""
        return Utils.count(self.map.values(), Country.can_disrupt)

    def countryResources(self, country):
        res = self.map[country].resources
        if self.map[country].oil:
            spikes = 0
            for event in self.lapsing:
                if event == "Oil Price Spike":
                    spikes += 1
            res += spikes
        return res

    def handleMuslimWoI(self, roll, country):
        if roll <= 3:
            self.outputToHistory("* WoI in %s failed." % country)
        elif roll == 4:
            if self.map[country].aid == 0:        # 20150131PS check for existing aid marker
                self.map[country].aid = 1
                self.outputToHistory("* WoI in %s adds Aid." % country, False)
                self.outputToHistory(self.map[country].countryStr(), True)
        else:
            if self.map[country].is_neutral():
                self.map[country].make_ally()
                self.outputToHistory("* WoI in %s succeeded - Alignment now Ally." % country, False)
                self.outputToHistory(self.map[country].countryStr(), True)
            elif self.map[country].is_ally():
                self.improveGovernance(country)
                self.outputToHistory("* WoI in %s succeeded - Governance now %s." % (country, self.map[country].govStr()), False)
                self.outputToHistory(self.map[country].countryStr(), True)

    def handleAlert(self, country):
        if self.map[country].plots > 0:
            self.map[country].plots -= 1
            self.outputToHistory("* Alert in %s - %d plot(s) remain." % (country, self.map[country].plots))

    def toggle_us_posture(self):
        """Switches the US posture between Hard and Soft"""
        if self.map["United States"].posture == "Hard":
            self.map["United States"].posture = "Soft"
        else:
            self.map["United States"].posture = "Hard"
        self.outputToHistory("* Reassessment = US Posture now %s" % self.map["United States"].posture)

    def handleRegimeChange(self, where, moveFrom, howMany, govRoll, prestigeRolls):
        if self.map["United States"].posture == "Soft":
            return
        if moveFrom == 'track':
            self.troops -= howMany
        else:
            self.map[moveFrom].changeTroops(-howMany)
        self.map[where].changeTroops(howMany)
        sleepers = self.map[where].sleeperCells
        self.map[where].sleeperCells = 0
        self.map[where].activeCells += sleepers
        self.map[where].make_ally()
        if govRoll <= 4:
            self.map[where].make_poor()
        else:
            self.map[where].make_fair()
        self.map[where].regimeChange = 1
        presMultiplier = 1
        if prestigeRolls[0] <= 4:
            presMultiplier = -1
        self.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
        self.outputToHistory("* Regime Change in %s" % where, False)
        self.outputToHistory(self.map[where].countryStr(), False)
        if moveFrom == "track":
            self.outputToHistory("%d Troops on Troop Track" % self.troops, False)
        else:
            self.outputToHistory("%d Troops in %s" % (self.map[moveFrom].troops(), moveFrom), False)
        self.outputToHistory("US Prestige %d" % self.prestige)
        if where == "Iraq" and "Iraqi WMD" in self.markers:
            self.markers.remove("Iraqi WMD")
            self.outputToHistory("Iraqi WMD no longer in play.", True)
        if where == "Libya" and "Libyan WMD" in self.markers:
            self.markers.remove("Libyan WMD")
            self.outputToHistory("Libyan WMD no longer in play.", True)

    def handleWithdraw(self, moveFrom, moveTo, howMany, prestigeRolls):
        if self.map["United States"].posture == "Hard":
            return
        self.map[moveFrom].changeTroops(-howMany)
        if moveTo == "track":
            self.troops += howMany
        else:
            self.map[moveTo].changeTroops(howMany)
        self.map[moveFrom].aid = 0
        self.map[moveFrom].besieged = 1
        presMultiplier = 1
        if prestigeRolls[0] <= 4:
            presMultiplier = -1
        self.changePrestige(min(prestigeRolls[1], prestigeRolls[2]) * presMultiplier)
        self.outputToHistory("* Withdraw troops from %s" % moveFrom, False)
        self.outputToHistory(self.map[moveFrom].countryStr(), False)
        if moveTo == "track":
            self.outputToHistory("%d Troops on Troop Track" % self.troops, False)
        else:
            self.outputToHistory("%d Troops in %s" % (self.map[moveTo].troops(), moveTo), False)
            self.outputToHistory(self.map[moveTo].countryStr(), False)
        self.outputToHistory("US Prestige %d" % self.prestige)

    def handleDisrupt(self, where):
        numToDisrupt = 1
        if "Al-Anbar" in self.markers and (where == "Iraq" or where == "Syria"):
            numToDisrupt = 1
        elif self.map[where].troops() >= 2 or self.map[where].posture == "Hard":
            numToDisrupt = min(2, self.map[where].totalCells(False))
        if self.map[where].totalCells(False) <= 0 and self.map[where].has_cadre():
            if "Al-Anbar" not in self.markers or (where != "Iraq" and where != "Syria"):
                self.outputToHistory("* Cadre removed in %s" % where)
                self.map[where].cadre = 0
        elif self.map[where].totalCells(False) <= numToDisrupt:
            self.outputToHistory("* %d cell(s) disrupted in %s." % (self.map[where].totalCells(False), where), False)
            if self.map[where].sleeperCells > 0:
                self.map[where].activeCells += self.map[where].sleeperCells
                numToDisrupt -= self.map[where].sleeperCells
                self.map[where].sleeperCells = 0
            if numToDisrupt > 0:
                self.map[where].activeCells -= numToDisrupt
                self.cells += numToDisrupt
                if self.map[where].activeCells < 0:
                    self.map[where].activeCells = 0
                if self.cells > 15:
                    self.cells = 15
            if self.map[where].totalCells(False) <= 0:
                self.outputToHistory("Cadre added in %s." % where, False)
                self.map[where].cadre = 1
            if self.map[where].troops() >= 2:
                self._increase_prestige(1)
                self.outputToHistory("US Prestige now %d." % self.prestige, False)
            self.outputToHistory(self.map[where].countryStr(), True)
        else:
            if self.map[where].activeCells == 0:
                self.map[where].activeCells += numToDisrupt
                self.map[where].sleeperCells -= numToDisrupt
                self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where), False)
            elif self.map[where].sleeperCells == 0:
                self.map[where].activeCells -= numToDisrupt
                self.cells += numToDisrupt
                self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where), False)
                if self.map[where].totalCells(False) <= 0:
                    self.outputToHistory("Cadre added in %s." % where, False)
                    self.map[where].cadre = 1
            else:
                if numToDisrupt == 1:
                    disStr = None
                    while not disStr:
                        input = self.my_raw_input("You can disrupt one cell. Enter a or s for either an active or sleeper cell: ")
                        input = input.lower()
                        if input == "a" or input == "s":
                            disStr = input
                    if disStr == "a":
                        self.map[where].activeCells -= numToDisrupt
                        self.cells += numToDisrupt
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                    else:
                        self.map[where].sleeperCells -= numToDisrupt
                        self.map[where].activeCells += numToDisrupt
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                else:
                    disStr = None
                    while not disStr:
                        if self.map[where].sleeperCells >= 2 and self.map[where].activeCells >= 2:
                            input = self.my_raw_input("You can disrupt two cells. Enter aa, as, or ss for active or sleeper cells: ")
                            input = input.lower()
                            if input == "aa" or input == "as" or input == "sa" or input == "ss":
                                disStr = input
                        elif self.map[where].sleeperCells >= 2:
                            input = self.my_raw_input("You can disrupt two cells. Enter as, or ss for active or sleeper cells: ")
                            input = input.lower()
                            if input == "as" or input == "sa" or input == "ss":
                                disStr = input
                        elif self.map[where].activeCells >= 2:
                            input = self.my_raw_input("You can disrupt two cells. Enter aa, or as for active or sleeper cells: ")
                            input = input.lower()
                            if input == "as" or input == "sa" or input == "aa":
                                disStr = input
                    if input == "aa":
                        self.map[where].activeCells -= 2
                        self.cells += 2
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                    elif input == "as" or input == "sa":
                        self.map[where].sleeperCells -= 1
                        self.cells += 1
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
                    else:
                        self.map[where].sleeperCells -= 2
                        self.map[where].activeCells += 2
                        self.outputToHistory("* %d cell(s) disrupted in %s." % (numToDisrupt, where))
            if self.map[where].troops() >= 2:
                self._increase_prestige(1)
                self.outputToHistory("US Prestige now %d." % self.prestige, False)
            self.outputToHistory(self.map[where].countryStr(), True)

    def executeJihad(self, country, rollList):
        successes = 0
        failures = 0
        target_country = self.map[country]
        originalBesieged = target_country.besieged  # 20150303PS save besieged status in case changed by major jihad failure
        for roll in rollList:
            if target_country.is_non_recruit_success(roll):
                successes += 1
            else:
                failures += 1
        target_country.reduce_aid_by(successes)  # Same for major and minor
        isMajorJihad = country in self.majorJihadPossible(len(rollList))
        self.outputToHistory("Jihad operation.  %d Successes rolled, %d Failures rolled" % (successes, failures), False)
        if isMajorJihad:  # all cells go active
            self.outputToHistory("* Major Jihad attempt in %s" % country, False)
            sleepers = target_country.sleeperCells
            target_country.sleeperCells = 0
            target_country.activeCells += sleepers
            self.outputToHistory("All cells go Active", False)
            if ((failures >= 2 and target_country.besieged == 0) or (failures == 3 and target_country.besieged == 1)) and (len(rollList) == 3) and target_country.is_poor():
                self.outputToHistory("Major Jihad Failure", False)
                target_country.besieged = 1
                self.outputToHistory("Besieged Regime", False)
                if target_country.is_adversary():
                    target_country.make_neutral()
                elif target_country.is_neutral():
                    target_country.make_ally()
                self.outputToHistory("Alignment %s" % target_country.alignment(), False)
        else:  # a cell is active for each roll
            self.outputToHistory("* Minor Jihad attempt in %s" % country, False)
            for i in range(len(rollList) - target_country.numActiveCells()):
                self.outputToHistory("Cell goes Active", False)
                target_country.sleeperCells -= 1
                target_country.activeCells += 1
        while successes > 0 and target_country.governance_is_better_than(POOR):
            target_country.worsenGovernance()
            successes -= 1
            self.outputToHistory("Governance to %s" % target_country.govStr(), False)
        if isMajorJihad and ((successes >= 2) or ((originalBesieged > 0) and (successes >= 1))):  # Major Jihad
            self.outputToHistory("Islamist Revolution in %s" % country, False)
            target_country.make_islamist_rule()
            self.outputToHistory("Governance to Islamist Rule", False)
            target_country.make_adversary()
            self.outputToHistory("Alignment to Adversary", False)
            target_country.regimeChange = 0
            if target_country.besieged > 0:
                self.outputToHistory("Besieged Regime marker removed.", False)

            target_country.besieged = 0
            target_country.aid = 0
            self.funding = min(9, self.funding + self.countryResources(country))
            self.outputToHistory("Funding now %d" % self.funding, False)
            if target_country.troops() > 0:
                self.prestige = 1
                self.outputToHistory("Troops present so US Prestige now 1", False)
        if self.ideology.failed_jihad_rolls_remove_cells():
            for i in range(failures):
                if target_country.numActiveCells() > 0:
                    target_country.removeActiveCell()
                else:
                    target_country.sleeperCells -= 1
                    self.outputToHistory("Sleeper cell Removed to Funding Track", False)
                    self.cells += 1
        self.outputToHistory(target_country.countryStr(), False)
        print ""

    def handleJihad(self, country, ops):
        """Returns number of unused Ops"""
        cells = self.map[country].totalCells(True)
        rollList = []
        for i in range(min(cells, ops)):
            rollList.append(random.randint(1, 6))
        self.executeJihad(country, rollList)
        return ops - len(rollList)

    def handleMinorJihad(self, countryList, ops):
        opsRemaining = ops
        for countryData in countryList:
            self.handleJihad(countryData[0], countryData[1])
            opsRemaining -= countryData[1]
        return opsRemaining

    def excessCellsNeededForMajorJihad(self):
        return self.ideology.excess_cells_for_major_jihad()

    def bhutto_in_play(self):
        return "Benazir Bhutto" in self.markers

    def majorJihadPossible(self, ops):
        """Return list of countries where major jihad is possible."""
        targets = []
        excessCellsNeeded = self.excessCellsNeededForMajorJihad()
        bhutto = self.bhutto_in_play()
        for country in self.map:
            if self.map[country].is_major_jihad_possible(ops, excessCellsNeeded, bhutto):
                targets.append(country)
        return targets

    def majorJihadChoice(self, ops):
        """Return AI choice country."""
        possible = self.majorJihadPossible(ops)
        if possible == []:
            return False
        else:
            if "Pakistan" in possible:
                return "Pakistan"
            else:
                maxResource = 0
                for country in possible:
                    if self.countryResources(country) > maxResource:
                        maxResource = self.countryResources(country)
                newPossible = []
                for country in possible:
                    if self.countryResources(country) == maxResource:
                        newPossible.append(country)
                return random.choice(newPossible)

    def minorJihadInGoodFairChoice(self, ops, isAbuGhurayb = False, isAlJazeera = False):
        possible = []
        for country in self.map:
            if isAbuGhurayb:
                if self.map[country].is_ally() and not self.map[country].is_islamist_rule():
                    possible.append(country)
            elif isAlJazeera:
                if country == "Saudi Arabia" or self.isAdjacent(country, "Saudi Arabia"):
                    if self.map[country].troops() > 0:
                        possible.append(country)
            elif (self.map[country].is_muslim()) and (self.map[country].is_good() or self.map[country].is_fair()) and (self.map[country].totalCells(True) > 0):
                if "Benazir Bhutto" in self.markers and country == "Pakistan":
                    continue
                possible.append(country)
        if len(possible) == 0:
            return False
        else:
            countryScores = {}
            for country in possible:
                if self.map[country].is_good():
                    countryScores[country] = 2000000
                else:
                    countryScores[country] = 1000000
                if country == "Pakistan":
                    countryScores[country] += 100000
                if self.map[country].aid > 0:
                    countryScores[country] += 10000
                if self.map[country].besieged > 0:
                    countryScores[country] += 1000
                countryScores[country] += (self.countryResources(country) * 100)
                countryScores[country] += random.randint(1, 99)
            countryOrder = []
            for country in countryScores:
                countryOrder.append((countryScores[country], (self.map[country].totalCells(True)), country))
            countryOrder.sort()
            countryOrder.reverse()
            returnList = []
            opsRemaining = ops
            for countryData in countryOrder:
                rolls = min(opsRemaining, countryData[1])
                returnList.append((countryData[2], rolls))
                opsRemaining -= rolls
                if opsRemaining <= 0:
                    break
            return returnList

    def _increase_prestige(self, amount):
        """Increases US prestige by the given amount (to no more than 12)"""
        assert amount > 0
        self.prestige += amount
        if self.prestige > 12:
            self.prestige = 12

    def _reduce_prestige(self, amount):
        """Reduces US prestige by the given amount (to no less than 1)"""
        assert amount > 0
        self.prestige -= amount
        if self.prestige < 1:
            self.prestige = 1

    def recruitChoice(self, ops, isMadrassas=False):
        self.debugPrint("DEBUG: recruit with remaining %d ops" % ops)
        self.debugPrint("DEBUG: recruit with remaining %d ops" % (2*ops))
        countryScores = {}
        for country_name in self.map:
            country = self.map[country_name]
            if country.can_recruit(isMadrassas):
                country_recruit_score = country.get_recruit_score(ops)
                if not country_recruit_score is None:
                    countryScores[country_name] = country_recruit_score
        for country in countryScores:
            self.debugPrint("c")
            if self.map[country].besieged > 0:
                countryScores[country] += 100000
            countryScores[country] += (1000 * (self.map[country].troops() + self.map[country].totalCells(True)))
            countryScores[country] += 100 * self.countryResources(country)
            countryScores[country] += random.randint(1, 99)
        countryOrder = []
        for country in countryScores:
            self.debugPrint("here: %d " % countryScores[country])
            if countryScores[country] > 0:
                countryOrder.append((countryScores[country], (self.map[country].totalCells(True)), country))
        countryOrder.sort()
        countryOrder.reverse()
        if countryOrder == []:
            self.debugPrint("d")
            return False
        else:
            self.debugPrint("e")
            return countryOrder[0][2]

    def executeRecruit(self, country, ops, rolls, recruitOverride=None, isJihadistVideos=False, isMadrassas=False):
        self.outputToHistory("* Recruit to %s" % country)
        cellsRequested = ops * self.ideology.recruits_per_success()
        cells = self.numCellsAvailable(isMadrassas or isJihadistVideos)
        cellsToRecruit = min(cellsRequested, cells)
        if self.map[country].regimeChange or self.map[country].is_islamist_rule():
            if self.map[country].regimeChange:
                self.outputToHistory("Recruit to Regime Change country automatically successful.", False)
            else:
                self.outputToHistory("Recruit to Islamist Rule country automatically successful.", False)
            self.cells -= cellsToRecruit
            self.map[country].sleeperCells += cellsToRecruit

            if cellsToRecruit == 0 and isJihadistVideos:
                self.map[country].cadre = 1
                self.outputToHistory("No cells available to recruit.  Cadre added.", False)
                self.outputToHistory(self.map[country].countryStr(), True)
                return ops - 1
            else:
                self.map[country].cadre = 0

            self.outputToHistory("%d sleeper cells recruited to %s." % (cellsToRecruit, country), False)
            self.outputToHistory(self.map[country].countryStr(), True)
            return ops - self.ideology.ops_to_recruit(cellsToRecruit)
        else:
            opsRemaining = ops
            i = 0

            if self.numCellsAvailable(isJihadistVideos) <= 0 and opsRemaining > 0:
                self.map[country].cadre = 1
                self.outputToHistory("No cells available to recruit. Cadre added.", False)
                self.outputToHistory(self.map[country].countryStr(), True)
                return ops - 1
            else:
                while self.numCellsAvailable(isMadrassas or isJihadistVideos) > 0 and opsRemaining > 0:
                    if self.map[country].is_recruit_success(rolls[i], recruitOverride):
                        cellsMoving = min(self.numCellsAvailable(isMadrassas or isJihadistVideos),
                                          self.ideology.recruits_per_success())
                        self.cells -= cellsMoving
                        self.map[country].sleeperCells += cellsMoving
                        self.map[country].cadre = 0
                        self.outputToHistory("Roll successful, %d sleeper cell(s) recruited." % cellsMoving, False)
                    else:
                        self.outputToHistory("Roll failed.", False)
                        if isJihadistVideos:
                            self.map[country].cadre = 1
                            self.outputToHistory("Cadre added.", False)
                    opsRemaining -= 1
                    i += 1
                self.outputToHistory(self.map[country].countryStr(), True)
                return opsRemaining

    def handleRecruit(self, ops, isMadrassas=False):
        self.debugPrint("recruit ops: ")
        self.debugPrint("DEBUG: recruit with remaining %d ops" % ops)
        country = self.recruitChoice(ops, isMadrassas)
        if not country:
            self.outputToHistory("* No countries qualify to Recruit.", True)
            return ops
        else:
            if isMadrassas:
                cells = self.cells
            else:
                if "GTMO" in self.lapsing:
                    self.outputToHistory("* Cannot Recruit due to GTMO.", True)
                    return ops
                cells = self.numCellsAvailable()
            if cells <= 0:
                self.outputToHistory("* No cells available to Recruit.", True)
                return ops
            else:
                rolls = []
                for i in range(ops):
                    rolls.append(random.randint(1, 6))
                return self.executeRecruit(country, ops, rolls, None, False, isMadrassas)

    def isAdjacent(self, here, there):
        if "Patriot Act" in self.markers:
            if here == "United States" or there == "United States":
                if here == "Canada" or there == "Canada":
                    return True
                else:
                    return False
        if self.map[here] in self.map[there].links:
            return True
        if self.map[here].schengen and self.map[there].schengen:
            return True
        if self.map[here].schengenLink and self.map[there].schengen:
            return True
        if self.map[here].schengen and self.map[there].schengenLink:
            return True
        return False

    def adjacentCountryHasCell(self, targetCountry):
        for country in self.map:
            if self.isAdjacent(targetCountry, country):
                if self.map[country].totalCells(True) > 0:
                    return True
        return False

    def inLists(self, country, lists):
        for list in lists:
            if country in lists:
                return True
        return False

    def countryDistance(self, start, end):
        if start == end:
            return 0
        distanceGroups = []
        distanceGroups.append([start])
        distance = 1
        while not self.inLists(end, distanceGroups):
            list = distanceGroups[distance - 1]
            nextWave = []
            for country in list:
                for subCountry in self.map:
                    if not self.inLists(subCountry, distanceGroups):
                        if self.isAdjacent(subCountry, country):
                            if subCountry == end:
                                return distance
                            if subCountry not in nextWave:
                                nextWave.append(subCountry)
            distanceGroups.append(nextWave)
            distance += 1

    def travelDestinationChooseBasedOnPriority(self, countryList):
        for country in countryList:
            if country == "Pakistan":
                return country
        maxResources = 0
        for country in countryList:
            if self.countryResources(country) > maxResources:
                maxResources = self.countryResources(country)
        maxdests = []
        for country in countryList:
            if self.countryResources(country) == maxResources:
                maxdests.append(country)
        return random.choice(maxdests)

    def travelDestinations(self, ops, isRadicalization=False):
        dests = []
        # A non-Islamist Rule country with Regime Change, Besieged Regime, or Aid, if any
        if not isRadicalization:
            subdests = []
            for country in self.map:
                if (not self.map[country].is_islamist_rule()) and ((self.map[country].besieged > 0) or (self.map[country].regimeChange > 0) or (self.map[country].aid > 0)):
                    if ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
            if len(subdests) == 1:
                dests.append(subdests[0])
            elif len(subdests) > 1:
                dests.append(self.travelDestinationChooseBasedOnPriority(subdests))
            if len(dests) == ops:
                return dests

        # A Poor country where Major Jihad would be possible if two (or fewer) cells were added.
        subdests = []
        for country in self.map:
            if (self.map[country].is_poor()) and (((self.map[country].totalCells(True) + 2) - self.map[country].troops()) >= self.excessCellsNeededForMajorJihad()):
                if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                    continue
                subdests.append(country)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(self.travelDestinationChooseBasedOnPriority(subdests))
        if len(dests) == ops:
            return dests

        # A Good or Fair Muslim country with at least one cell adjacent.
        subdests = []
        for country in self.map:
            if (self.map[country].is_good() or self.map[country].is_fair()) and self.map[country].is_muslim():
                if self.adjacentCountryHasCell(country):
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(self.travelDestinationChooseBasedOnPriority(subdests))
        if len(dests) == ops:
            return dests

        # An unmarked non-Muslim country if US Posture is Hard, or a Soft non-Muslim country if US Posture is Soft.
        subdests = []
        if self.map["United States"].posture == "Hard":
            for country in self.map:
                if self.map[country].type == "Non-Muslim" and self.map[country].posture == "":
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
        else:
            for country in self.map:
                if country != "United States" and self.map[country].type == "Non-Muslim" and self.map[country].posture == "Soft":
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.adjacentCountryHasCell(country)):
                        continue
                    subdests.append(country)
        if len(subdests) == 1:
            dests.append(subdests[0])
        elif len(subdests) > 1:
            dests.append(random.choice(subdests))
        if len(dests) == ops:
            return dests

            # Random
        if (not isRadicalization) and ("Biometrics" in self.lapsing):
            subdests = []
            for country in self.map:
                if self.adjacentCountryHasCell(country):
                    subdests.append(country)
            if len(subdests) > 0:
                while len(dests) < ops:
                    dests.append(random.choice(subdests))
        else:
            while len(dests) < ops:
                dests.append(random.choice(self.map.keys()))

        return dests

    def names_of_countries(self, predicate):
        """Returns the names of countries matching the given predicate"""
        return [country for country in self.map if predicate(self.map[country])]

    def travelDestinationsSchengenVisas(self):
        """
        Returns the names of countries that are valid travel
        destinations for the Schengen Visas event
        """
        if self.map["United States"].posture == "Hard":
            candidates = self.names_of_countries(lambda c: c.schengen and c.posture == '')
        else:
            candidates = self.names_of_countries(lambda c: c.schengen and c.posture == 'Soft')
        if len(candidates) == 1:
            return [candidates[0], candidates[0]]  # yes, same one twice
        if len(candidates) > 1:
            return self.randomizer.pick(2, candidates)
        schengens = self.names_of_countries(lambda c: c.schengen)
        return self.randomizer.pick(2, schengens)

    def travelSourceChooseBasedOnPriority(self, countryList, i, destinations):
        subPossibles = []
        for country in countryList:
            if self.map[country].activeCells > 0:
                subPossibles.append(country)
        if len(subPossibles) == 1:
            return subPossibles[0]
        elif len(subPossibles) > 1:
            return random.choice(subPossibles)
        else:
            subPossibles = []
            for country in countryList:
                notAnotherDest = True
                for j in range(len(destinations)):
                    if (i != j) and (country == destinations[j]):
                        subPossibles.append(country)
        if len(subPossibles) == 1:
            return subPossibles[0]
        elif len(subPossibles) > 1:
            return random.choice(subPossibles)
        else:
            return random.choice(countryList)

    def travelSourceBoxOne(self, i, destinations, sources, ops, isRadicalization=False):
        possibles = []
        for country in self.map:
            if self.map[country].is_islamist_rule():
                numTimesIsSource = 0
                for source in sources:
                    if source == country:
                        numTimesIsSource += 1
                if ((self.map[country].sleeperCells + self.map[country].activeCells) - numTimesIsSource) > ops:
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                        continue
                    possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)

    def travelSourceBoxTwo(self, i, destinations, sources, isRadicalization=False):
        possibles = []
        for country in self.map:
            if self.map[country].regimeChange > 0:
                numTimesIsSource = 0
                for source in sources:
                    if source == country:
                        numTimesIsSource += 1
                if ((self.map[country].sleeperCells + self.map[country].activeCells) - numTimesIsSource) > self.map[country].troops():
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                        continue
                    possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)

    def travelSourceBoxThree(self, i, destinations, sources, isRadicalization=False):
        possibles = []
        for country in self.map:
            if self.isAdjacent(destinations[i], country):
                adjacent = self.map[country]
                numTimesIsSource = 0
                for source in sources:
                    if source == adjacent.name:
                        numTimesIsSource += 1
                if ((adjacent.sleeperCells + adjacent.activeCells) - numTimesIsSource) > 0:
                    if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                        continue
                    possibles.append(adjacent.name)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)

    def travelSourceBoxFour(self, i, destinations, sources, isRadicalization=False):
        possibles = []
        for country in self.map:
            numTimesIsSource = 0
            for source in sources:
                if source == country:
                    numTimesIsSource += 1
            if ((self.map[country].sleeperCells + self.map[country].activeCells) - numTimesIsSource) > 0:
                if (not isRadicalization) and ("Biometrics" in self.lapsing) and (not self.isAdjacent(country, destinations[i])):
                    continue
                possibles.append(country)
        if len(possibles) == 0:
            return False
        if len(possibles) == 1:
            return possibles[0]
        else:
            return self.travelSourceChooseBasedOnPriority(possibles, i, destinations)

    def travelSources(self, destinations, ops, isRadicalization=False):
        sources = []
        for i in range(len(destinations)):
            source = self.travelSourceBoxOne(i, destinations, sources, ops, isRadicalization)
            if source:
                sources.append(source)
            else:
                source = self.travelSourceBoxTwo(i, destinations, sources, isRadicalization)
                if source:
                    sources.append(source)
                else:
                    source = self.travelSourceBoxThree(i, destinations, sources, isRadicalization)
                    if source:
                        sources.append(source)
                    else:
                        source = self.travelSourceBoxFour(i, destinations, sources, isRadicalization)
                        if source:
                            sources.append(source)
        return sources

    def testCountry(self, country):
        # Country testing if necessary
        if self.map[country].type == "Non-Muslim" and self.map[country].posture == "":
            testRoll = random.randint(1, 6)
            if testRoll <= 4:
                self.map[country].posture = "Soft"
            else:
                self.map[country].posture = "Hard"
            self.outputToHistory("%s tested, posture %s" % (self.map[country].name, self.map[country].posture), False)
        elif self.map[country].is_ungoverned():
            testRoll = random.randint(1, 6)
            if testRoll <= 4:
                self.map[country].make_poor()
            else:
                self.map[country].make_fair()
            self.map[country].make_neutral()
            self.outputToHistory("%s tested, governance %s" % (self.map[country].name, self.map[country].govStr()), False)

    def getCountriesWithUSPostureByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if (country != "United States") and (self.map[country].posture == self.map["United States"].posture):
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict

    def getCountriesWithTroopsByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if self.map[country].troops() > 0:
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict

    def getCountriesWithAidByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if self.map[country].aid > 0:
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict

    def getNonMuslimCountriesByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if (country != "United States") and (self.map[country].type == "Non-Muslim"):
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict

    def getMuslimCountriesByGovernance(self):
        dict = {GOOD: [], FAIR: [], POOR: []}
        for country in self.map:
            if self.map[country].type != "Non-Muslim":
                if self.map[country].is_good():
                    dict[GOOD].append(country)
                elif self.map[country].is_fair():
                    dict[FAIR].append(country)
                elif self.map[country].is_poor():
                    dict[POOR].append(country)
        return dict

    def handleTravel(self, ops, isRadicalization=False, isSchengenVisas=False, isCleanOperatives=False):
        if isSchengenVisas:
            destinations = self.travelDestinationsSchengenVisas()
        elif isCleanOperatives:
            destinations = ["United States", "United States"]
        else:
            destinations = self.travelDestinations(ops, isRadicalization)
        sources = self.travelSources(destinations, ops, isRadicalization)
        if not isRadicalization and not isSchengenVisas and not isCleanOperatives:
            self.outputToHistory("* Cells Travel", False)
        for i in range(len(sources)):
            self.outputToHistory("->Travel from %s to %s." % (sources[i], destinations[i]), False)
            success = False
            displayStr = "BLAH!!"
            if isRadicalization:
                success = True
                displayStr = ("Travel by Radicalization is automatically successful.")
            elif isSchengenVisas:
                success = True
                displayStr = ("Travel by Schengen Visas is automatically successful.")
            elif isCleanOperatives:
                success = True
                displayStr = ("Travel by Clean Operatives is automatically successful.")
            else:
                if sources[i] == destinations[i]:
                    success = True
                    displayStr = ("Travel within country automatically successful.")
                else:
                    if self.isAdjacent(sources[i], destinations[i]):
                        if not "Biometrics" in self.lapsing:
                            success = True
                            displayStr = ("Travel to adjacent country automatically successful.")
                        else:
                            roll = random.randint(1, 6)
                            if self.map[destinations[i]].is_non_recruit_success(roll):
                                success = True
                                displayStr = ("Travel roll needed due to Biometrics - roll successful.")
                            else:
                                displayStr = ("Travel roll needed due to Biometrics -  roll failed, cell to funding track.")
                    else:
                        roll = random.randint(1, 6)
                        if self.map[destinations[i]].is_non_recruit_success(roll):
                            success = True
                            displayStr = ("Travel roll successful.")
                        else:
                            displayStr = ("Travel roll failed, cell to funding track.")
            self.outputToHistory(displayStr, True)
            self.testCountry(destinations[i])
            if success:
                if self.map[sources[i]].activeCells > 0:
                    self.map[sources[i]].activeCells -= 1
                else:
                    self.map[sources[i]].sleeperCells -= 1
                self.map[destinations[i]].sleeperCells += 1
                self.outputToHistory(self.map[sources[i]].countryStr(), False)
                self.outputToHistory(self.map[destinations[i]].countryStr(), True)
            else:
                if self.map[sources[i]].activeCells > 0:
                    self.map[sources[i]].activeCells -= 1
                else:
                    self.map[sources[i]].sleeperCells -= 1
                self.cells += 1
                self.outputToHistory(self.map[sources[i]].countryStr(), True)
        return ops - len(sources)

    def placePlots(self, country, rollPosition, plotRolls, isMartyrdomOperation=False, isDanishCartoons=False, isKSM=False):
        if (self.map[country].totalCells(True)) > 0:
            if isMartyrdomOperation:
                self.removeCell(country, "Jihadist")    # 20150131PS added side
                self.outputToHistory("Place 2 available plots in %s." % country, False)
                self.map[country].plots += 2
                rollPosition = 1
            elif isDanishCartoons:
                if self.numIslamistRule() > 0:
                    self.outputToHistory("Place any available plot in %s." % country, False)
                else:
                    self.outputToHistory("Place a Plot 1 in %s." % country, False)
                self.map[country].plots += 1
                rollPosition = 1
            elif isKSM:
                if not self.map[country].is_islamist_rule():
                    self.outputToHistory("Place any available plot in %s." % country, False)
                    self.map[country].plots += 1
                    rollPosition = 1
            else:
                opsRemaining = len(plotRolls) - rollPosition
                cellsAvailable = self.map[country].totalCells(True)
                plotsToPlace = min(cellsAvailable, opsRemaining)
                self.outputToHistory("--> %s plot attempt(s) in %s." % (plotsToPlace, country), False)
                successes = 0
                failures = 0
                for i in range(rollPosition, rollPosition + plotsToPlace):
                    if self.map[country].is_non_recruit_success(plotRolls[i]):
                        successes += 1
                    else:
                        failures += 1
                self.outputToHistory("Plot rolls: %d Successes rolled, %d Failures rolled" % (successes, failures), False)
                for i in range(plotsToPlace - self.map[country].numActiveCells()):
                    self.outputToHistory("Cell goes Active", False)
                    self.map[country].sleeperCells -= 1
                    self.map[country].activeCells += 1
                plots_placed = successes * self.ideology.plots_per_success()
                self.map[country].plots += plots_placed
                self.outputToHistory("%d Plot(s) placed in %s." % (plots_placed, country), False)
                if "Abu Sayyaf" in self.markers and country == "Philippines" and self.map[country].troops() <= self.map[country].totalCells() and successes > 0:
                    self.outputToHistory("Prestige loss due to Abu Sayyaf.", False)
                    self.changePrestige(-successes)
                if "NEST" in self.markers and country == "Unites States":
                    self.outputToHistory("NEST in play. If jihadists have WMD, all plots in the US placed face up.", False)
                self.outputToHistory(self.map[country].countryStr(), True)
                rollPosition += plotsToPlace
        return rollPosition

    def handlePlotPriorities(self, countriesDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation=False, isDanishCartoons=False, isKSM=False):
        if isOps:
            if len(countriesDict[FAIR]) > 0:
                targets = countriesDict[FAIR]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
            if len(countriesDict[GOOD]) > 0:
                targets = countriesDict[GOOD]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
        else:
            if len(countriesDict[GOOD]) > 0:
                targets = countriesDict[GOOD]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
            if len(countriesDict[FAIR]) > 0:
                targets = countriesDict[FAIR]
                random.shuffle(targets)
                i = 0
                while rollPosition < ops and i < len(targets):
                    rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                    i += 1
            if rollPosition == ops:
                return rollPosition
        if len(countriesDict[POOR]) > 0:
            targets = countriesDict[POOR]
            random.shuffle(targets)
            i = 0
            while rollPosition < ops and i < len(targets):
                rollPosition = self.placePlots(targets[i], rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                i += 1
        return rollPosition

    def executePlot(self, ops, isOps, plotRolls, isMartyrdomOperation=False, isDanishCartoons=False, isKSM=False):
        if not isMartyrdomOperation and not isDanishCartoons and not isKSM:
            self.outputToHistory("* Jihadists Plotting", False)
        # In US
        self.debugPrint("DEBUG: In US")
        rollPosition = self.placePlots("United States", 0, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
        if rollPosition == ops:
            return 0
        if self.prestige >= 4:
            # Prestige high
            self.debugPrint("DEBUG: Prestige high")
            if ("Abu Sayyaf" in self.markers) and ((self.map["Philippines"].totalCells(True)) >= self.map["Philippines"].troops()):
                # In Philippines
                self.debugPrint("DEBUG: Philippines")
                rollPosition = self.placePlots("Philippines", rollPosition, plotRolls, isMartyrdomOperation, isDanishCartoons, isKSM)
                if rollPosition == ops:
                    return 0
            # With troops
            self.debugPrint("DEBUG: troops")
            troopDict = self.getCountriesWithTroopsByGovernance()
            rollPosition = self.handlePlotPriorities(troopDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
        # No GWOT Penalty
        if self.gwotPenalty() >= 0:
            self.debugPrint("DEBUG: No GWOT Penalty")
            postureDict = self.getCountriesWithUSPostureByGovernance()
            rollPosition = self.handlePlotPriorities(postureDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
        # With aid
        self.debugPrint("DEBUG: aid")
        aidDict = self.getCountriesWithAidByGovernance()
        rollPosition = self.handlePlotPriorities(aidDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
        if rollPosition == ops:
            return 0
        # Funding < 9
        if self.funding < 9:
            self.debugPrint("DEBUG: Funding < 9")
            nonMuslimDict = self.getNonMuslimCountriesByGovernance()
            rollPosition = self.handlePlotPriorities(nonMuslimDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
            muslimDict = self.getMuslimCountriesByGovernance()
            rollPosition = self.handlePlotPriorities(muslimDict, ops, rollPosition, plotRolls, isOps, isMartyrdomOperation, isDanishCartoons, isKSM)
            if rollPosition == ops:
                return 0
        return len(plotRolls) - rollPosition

    def handlePlot(self, ops, isOps):
        plotRolls = []
        for i in range(ops):
            plotRolls.append(random.randint(1, 6))
        return self.executePlot(ops, isOps, plotRolls)

    def place_cell(self, country_name):
        """Places a cell from the funding track into the given country"""
        country = self.map[country_name]
        country.cadre = 0
        country.sleeperCells += 1
        self.cells -= 1
        self.testCountry(country_name)
        self.outputToHistory("--> Sleeper Cell placed in %s." % country_name, True)
        self.outputToHistory(self.map[country_name].countryStr(), True)

    def handleRadicalization(self, ops):
        self.outputToHistory("* Radicalization with %d ops." % ops, False)
        opsRemaining = ops
        # First box
        if opsRemaining > 0:
            if self.cells > 0:
                country_name = self.randomizer.pick_one(self.map.keys())
                self.place_cell(country_name)
                opsRemaining -= 1
                # Second box
        if opsRemaining > 0:
            if self.cells < 15:
                self.handleTravel(1, True)
                opsRemaining -= 1
                # Third box
        if opsRemaining > 0:
            if self.funding < 9:
                possibles = []
                for country in self.map:
                    if not self.map[country].is_islamist_rule():
                        if (self.map[country].totalCells(True)) > 0:
                            possibles.append(country)
                if len(possibles) > 0:
                    location = random.choice(possibles)
                    self.testCountry(location)
                    self.map[location].plots += 1
                    self.outputToHistory("--> Plot placed in %s." % location, True)
                    opsRemaining -= 1
                    # Fourth box
        while opsRemaining > 0:
            possibles = []
            for country in self.map:
                if (self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni") and (self.map[country].is_good() or self.map[country].is_fair()):
                    possibles.append(country)
            if len(possibles) == 0:
                self.outputToHistory("--> No remaining Good or Fair countries.", True)
                break
            else:
                location = random.choice(possibles)
                self.map[location].worsenGovernance()
                self.outputToHistory("--> Governance in %s worsens to %s." % (location, self.map[location].govStr()), True)
                self.outputToHistory(self.map[location].countryStr(), True)
                opsRemaining -= 1

    def resolvePlot(self, country, plotType, postureRoll, usPrestigeRolls, schCountries, schPostureRolls, govRolls, isBacklash=False):
        self.outputToHistory("--> Resolve \"%s\" plot in %s" % (str(plotType), country), False)
        if country == "United States":
            self._resolve_plot_in_us(plotType, postureRoll, usPrestigeRolls)
        elif self.map[country].type == "Non-Muslim":
            self._resolve_plot_in_non_muslim_country(country, plotType, postureRoll, schCountries, schPostureRolls)
        else:  # e.g. Iran
            self._resolve_plot_in_muslim_country(country, govRolls, isBacklash, plotType)
        self.map[country].remove_plot_marker()

    def _resolve_plot_in_non_muslim_country(self, country, plotType, postureRoll, schCountries, schPostureRolls):
        if country == "Israel" and "Abbas" in self.markers:
            self.markers.remove("Abbas")
            self.outputToHistory("Abbas no longer in play.", True)
        if country == "India" and "Indo-Pakistani Talks" in self.markers:
            self.markers.remove("Indo-Pakistani Talks")
            self.outputToHistory("Indo-Pakistani Talks no longer in play.", True)
        if plotType == "WMD":
            self.funding = 9
        else:
            if self.map[country].is_good():
                self.changeFunding(plotType * 2)
            else:
                self.changeFunding(plotType)
        self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
        if country != "Israel":
            if postureRoll <= 4:
                self.map[country].posture = "Soft"
            else:
                self.map[country].posture = "Hard"
            self.outputToHistory("%s Posture now %s" % (country, self.map[country].posture), True)
        if self.map[country].troops() > 0:
            if plotType == "WMD":
                self.prestige = 1
            else:
                self._reduce_prestige(1)
            self.outputToHistory("Troops present so US Prestige now %d" % self.prestige, False)
        if self.map[country].schengen:
            for i in range(len(schCountries)):
                if schPostureRolls[i] <= 4:
                    self.map[schCountries[i]].posture = "Soft"
                else:
                    self.map[schCountries[i]].posture = "Hard"
                self.outputToHistory("%s Posture now %s" % (schCountries[i], self.map[schCountries[i]].posture), False)
        self.outputToHistory("", False)

    def _resolve_plot_in_muslim_country(self, country, govRolls, isBacklash, plotType):
        if not isBacklash:
            if self.map[country].is_good():
                self.changeFunding(2)
            else:
                self.changeFunding(1)
            self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
        else:
            if plotType == "WMD":
                self.funding = 1
            else:
                self.funding -= 1
                if self.map[country].is_good():
                    self.funding -= 1
                if self.funding < 1:
                    self.funding = 1
            self.outputToHistory("BACKLASH: Jihadist Funding now %d" % self.funding, False)
        if self.map[country].troops() > 0:
            if plotType == "WMD":
                self.prestige = 1
            else:
                self._reduce_prestige(1)
            self.outputToHistory("Troops present so US Prestige now %d" % self.prestige, False)
        if country != "Iran":
            successes = 0
            failures = 0
            for roll in govRolls:
                if self.map[country].is_non_recruit_success(roll):
                    successes += 1
                else:
                    failures += 1
            self.outputToHistory("Governance rolls: %d Successes rolled, %d Failures rolled" % (successes, failures),
                                 False)
            if self.map[country].aid and successes > 0:
                self.map[country].aid -= successes  # 20150131PS remove 1 aid for each success
                if self.map[country].aid < 0:
                    self.map[country].aid = 0
                self.outputToHistory("Aid removed.", False)
            if self.map[country].is_poor() and successes > 0:
                self.outputToHistory("Governance stays at %s" % self.map[country].govStr(), True)
            while successes > 0 and self.map[country].governance_is_better_than(POOR):
                self.map[country].worsenGovernance()
                successes -= 1
                self.outputToHistory("Governance to %s" % self.map[country].govStr(), True)

    def _resolve_plot_in_us(self, plotType, postureRoll, usPrestigeRolls):
        if plotType == "WMD":
            self.gameOver = True
            self.outputToHistory("== GAME OVER - JIHADIST AUTOMATIC VICTORY ==", True)
        else:
            self.funding = 9
            self.outputToHistory("Jihadist Funding now 9", False)
            presMultiplier = 1
            if usPrestigeRolls[0] <= 4:
                presMultiplier = -1
            self.changePrestige(min(usPrestigeRolls[1], usPrestigeRolls[2]) * presMultiplier)
            self.outputToHistory("US Prestige now %d" % self.prestige, False)
            if postureRoll <= 4:
                self.map["United States"].posture = "Soft"
            else:
                self.map["United States"].posture = "Hard"
            self.outputToHistory("US Posture now %s" % self.map["United States"].posture, True)

    def eventPutsCell(self, cardNum):
        return self.deck[str(cardNum)].putsCell(self)

    def playableNonUSEvent(self, cardNum):
        return self.deck[str(cardNum)].type != "US" and  self.deck[str(cardNum)].playable("Jihadist", self, False)

    def playableUSEvent(self, cardNum):
        return self.deck[str(cardNum)].type == "US" and  self.deck[str(cardNum)].playable("US", self, False)

    def aiFlowChartTop(self, cardNum):
        self.debugPrint("DEBUG: START")
        self.debugPrint("DEBUG: Playable Non-US event? [1]")
        if self.playableNonUSEvent(cardNum):
            self.debugPrint("DEBUG: YES")
            self.outputToHistory("Playable Non-US Event.", False)
            self.debugPrint("Event Recruits or places cell? [2]")
            if self.eventPutsCell(cardNum):
                self.debugPrint("DEBUG: YES")
                self.debugPrint("Track has cell? [3]")
                if self.cells > 0:
                    self.debugPrint("DEBUG: YES")
                    self.aiFlowChartPlayEvent(cardNum)
                else:
                    self.debugPrint("DEBUG: NO")
                    self.debugPrint("DEBUG: Radicalization [4]")
                    self.handleRadicalization(self.deck[str(cardNum)].ops)
            else:
                self.debugPrint("DEBUG: NO")
                self.aiFlowChartPlayEvent(cardNum)
        else:
            self.debugPrint("DEBUG: NO")
            self.debugPrint("DEBUG: Playble US event? [7]")
            if self.playableUSEvent(cardNum):
                self.debugPrint("DEBUG: YES")
                self.debugPrint("DEBUG: Plot Here [5]")
                self.outputToHistory("Playable US Event.", False)
                unusedOps = self.handlePlot(self.deck[str(cardNum)].ops, True)
                if unusedOps > 0:
                    self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                    self.handleRadicalization(unusedOps)
                self.debugPrint("DEBUG: END")
            else:
                self.debugPrint("DEBUG: NO")
                self.outputToHistory("Unplayable Event. Using Ops for Operations.", False)
                self.aiFlowChartMajorJihad(cardNum)

    def aiFlowChartPlayEvent(self, cardNum):
        self.debugPrint("Play Event [6]")
        self.deck[str(cardNum)].playEvent("Jihadist", self)
        self.debugPrint("Unassociated Event? [8]")
        if self.deck[str(cardNum)].type == "Unassociated":
            self.debugPrint("DEBUG: YES")
            self.outputToHistory("Unassociated event now being used for Ops.", False)
            self.aiFlowChartMajorJihad(cardNum)
        else:
            self.debugPrint("DEBUG: NO")
            self.debugPrint("end [9]")

    def aiFlowChartMajorJihad(self, cardNum):
        self.debugPrint("DEBUG: Major Jihad success possible? [10]")
        country = self.majorJihadChoice(self.deck[str(cardNum)].ops)
        if country:
            self.debugPrint("DEBUG: YES")
            self.debugPrint("DEBUG: Major Jihad [11]")
            unusedOps = self.handleJihad(country, self.deck[str(cardNum)].ops)
            if unusedOps > 0:
                self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                self.handleRadicalization(unusedOps)
        else:
            self.debugPrint("DEBUG: NO")
            self.debugPrint("DEBUG: Jihad possible in Good/Fair? [12]")
            countryList = self.minorJihadInGoodFairChoice(self.deck[str(cardNum)].ops)
            if countryList:
                self.debugPrint("DEBUG: YES")
                unusedOps = self.handleMinorJihad(countryList, self.deck[str(cardNum)].ops)
                if unusedOps > 0:
                    self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                    self.handleRadicalization(unusedOps)
            else:
                self.debugPrint("DEBUG: NO")
                self.debugPrint("DEBUG: Cells Available? [14]")
                if self.numCellsAvailable() > 0:
                    self.debugPrint("DEBUG: YES")
                    self.debugPrint("DEBUG: Recruit [15]")
                    unusedOps = self.handleRecruit(self.deck[str(cardNum)].ops)
                    if unusedOps > 0:
                        self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                        self.handleRadicalization(unusedOps)
                else:
                    self.debugPrint("DEBUG: NO")
                    self.debugPrint("DEBUG: Travel [16]")
                    unusedOps = self.handleTravel(self.deck[str(cardNum)].ops)
                    if unusedOps > 0:
                        self.debugPrint("DEBUG: Radicalization with remaining %d ops" % unusedOps)
                        self.handleRadicalization(unusedOps)

    def executeNonMuslimWOI(self, country, postureRoll):
        if postureRoll > 4:
            self.map[country].posture = "Hard"
            self.outputToHistory("* War of Ideas in %s - Posture Hard" % country, False)
            if self.map["United States"].posture == "Hard":
                self.changePrestige(1)
        else:
            self.map[country].posture = "Soft"
            self.outputToHistory("* War of Ideas in %s - Posture Soft" % country, False)
            if self.map["United States"].posture == "Soft":
                self.changePrestige(1)

    def executeCardEuroIslam(self, posStr):
        self.map["Benelux"].posture = posStr
        if self.numIslamistRule() == 0:
            self.funding -= 1
            if self.funding < 1:
                self.funding = 1
            self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
        self.outputToHistory(self.map["Benelux"].countryStr(), True)

    def executeCardLetsRoll(self, plotCountry, postureCountry, postureStr):
        self.map[plotCountry].plots = max(0, self.map[plotCountry].plots - 1)
        self.outputToHistory("Plot removed from %s." % plotCountry, False)
        self.map[postureCountry].posture = postureStr
        self.outputToHistory("%s Posture now %s." % (postureCountry, postureStr), False)
        self.outputToHistory(self.map[plotCountry].countryStr(), False)
        self.outputToHistory(self.map[postureCountry].countryStr(), True)

    def executeCardHEU(self, country, roll):
        if self.map[country].is_non_recruit_success(roll):
            self.outputToHistory("Add a WMD to available Plots.", True)
        else:
            self.removeCell(country, "Jihadist")    # 20150131PS added side

    def executeCardUSElection(self, postureRoll):
        if postureRoll <= 4:
            self.map["United States"].posture = "Soft"
            self.outputToHistory("United States Posture now Soft.", False)
        else:
            self.map["United States"].posture = "Hard"
            self.outputToHistory("United States Posture now Hard.", False)
        if self.gwotPenalty() == 0:
            self.changePrestige(1)
        else:
            self.changePrestige(-1)

    def listCountriesInParam(self, needed=None):
        print ""
        print "Countries"
        print "---------"
        for country in needed:
            self.map[country].printCountry()
        print ""

    def listCountriesWithTroops(self, needed=None):
        print ""
        print "Countries with Troops"
        print "---------------------"
        if needed is None:
            needed = 0
        if self.troops > needed:
            print "Troop Track: %d" % self.troops
        for country in self.map:
            if self.map[country].troops() > needed:
                print "%s: %d" % (country, self.map[country].troops())
        print ""

    def _can_deploy_to(self, country_name):
        """Indicates whether the US player can peacefully deploy troops to the named country"""
        return self.map[country_name].is_ally() or ("Abu Sayyaf" in self.markers and country_name == "Philippines")

    def listDeployOptions(self, na=None):
        print ""
        print "Deploy Options"
        print "--------------"
        for country in self.map:
            if self._can_deploy_to(country):
                print "%s: %d troops" % (country, self.map[country].troops())
        print ""

    def listDisruptableCountries(self, na = None):
        print ""
        print "Disruptable Countries"
        print "--------------------"
        for country in self.map:
            if self.map[country].can_disrupt():
                print self.map[country].get_disrupt_summary()
        print ""

    def listWoICountries(self, na=None):
        print ""
        print "War of Ideas Eligible Countries"
        print "-------------------------------"
        for country in self.map:
            if self.map[country].is_neutral() or self.map[country].is_ally() or self.map[country].is_ungoverned():
                print "%s, %s %s - %d Active Cells, %d Sleeper Cells, %d Cadre, %d troops" % (country, self.map[country].govStr(), self.map[country].__alignment, self.map[country].activeCells, self.map[country].sleeperCells, self.map[country].cadre, self.map[country].troops())
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "Hard":
                print "%s, Posture %s" % (country, self.map[country].posture)
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "Soft":
                print "%s, Posture %s" % (country, self.map[country].posture)
        for country in self.map:
            if self.map[country].type == "Non-Muslim" and country != "United States" and self.map[country].posture == "":
                print "%s, Untested" % country

    def listPlotCountries(self, na=None):
        print ""
        print "Countries with Active Plots"
        print "---------------------------"
        for country in self.map:
            if self.map[country].plots > 0:
                self.map[country].printCountry()
        print ""

    def listIslamistCountries(self, na=None):
        print ""
        print "Islamist Rule Countries"
        print "-----------------------"
        for country in self.map:
            if self.map[country].is_islamist_rule():
                self.map[country].printCountry()
        print ""

    def listRegimeChangeCountries(self, na=None):
        print ""
        print "Regime Change Countries"
        print "-----------------------"
        for country in self.map:
            if self.map[country].regimeChange > 0:
                self.map[country].printCountry()
        print ""

    def listRegimeChangeWithTwoCells(self, na=None):
        print ""
        print "Regime Change Countries with Two Cells"
        print "--------------------------------------"
        for country in self.map:
            if self.map[country].regimeChange > 0:
                if self.map[country].totalCells() >= 2:
                    self.map[country].printCountry()
        print ""

    def listCountriesWithCellAndAdjacentTroops(self, na=None):
        print ""
        print "Countries with Cells and with Troops or adjacent to Troops"
        print "----------------------------------------------------------"
        for country in self.map:
            if self.map[country].totalCells(True) > 0:
                if self.map[country].troops() > 0:
                    self.map[country].printCountry()
                else:
                    for subCountry in self.map:
                        if subCountry != country:
                            if self.map[subCountry].troops() > 0 and self.isAdjacent(country, subCountry):
                                self.map[country].printCountry()
                                break
        print ""

    def listAdversaryCountries(self, na=None):
        print ""
        print "Adversary Countries"
        print "-------------------"
        for country in self.map:
            if self.map[country].is_adversary():
                self.map[country].printCountry()
        print ""

    def listGoodAllyPlotCountries(self, na=None):
        print ""
        print "Ally or Good Countries with Plots"
        print "---------------------------------"
        for country in self.map:
            if self.map[country].plots > 0:
                if self.map[country].is_ally() or self.map[country].is_good():
                    self.map[country].printCountry()
        print ""

    def listMuslimCountriesWithCells(self, na=None):
        print ""
        print "Muslim Countries with Cells"
        print "---------------------------"
        for country in self.map:
            if self.map[country].totalCells(True) > 0:
                if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
                    self.map[country].printCountry()
        print ""

    def listBesiegedCountries(self, na=None):
        print ""
        print "Besieged Regimes"
        print "----------------"
        for country in self.map:
            if self.map[country].besieged > 0:
                self.map[country].printCountry()
        print ""

    def listShiaMixRegimeChangeCountriesWithCells(self, na=None):
        print ""
        print "Shia-Mix Regime Change Countries with Cells"
        print "-------------------------------------------"
        for country in self.map:
            if self.map[country].type == "Shia-Mix":
                if self.map[country].regimeChange > 0:
                    if (self.map[country].totalCells(True)) > 0:
                        self.map[country].printCountry()
        print ""

    def listShiaMixCountries(self, na=None):
        print ""
        print "Shia-Mix Countries"
        print "------------------"
        for country in self.map:
            if self.map[country].type == "Shia-Mix":
                self.map[country].printCountry()
        print ""

    def listShiaMixCountriesWithCellsTroops(self, na=None):
        print ""
        print "Shia-Mix Countries with Cells and Troops"
        print "----------------------------------------"
        for country in self.map:
            if self.map[country].type == "Shia-Mix":
                if self.map[country].troops() > 0 and self.map[country].totalCells() > 0:
                    self.map[country].printCountry()
        print ""

    def listSchengenCountries(self, na=None):
        print ""
        print "Schengen Countries"
        print "------------------"
        for country in self.map:
            if self.map[country].schengen > 0:
                self.map[country].printCountry()
        print ""

    def listHambali(self, na=None):
        print ""
        print "Indonesia or adjacent country with cell and Ally or Hard"
        print "--------------------------------------------------------"
        possibles = ["Indonesia/Malaysia"]
        for countryObj in self.map["Indonesia/Malaysia"].links:
            possibles.append(countryObj.name)
        for country in possibles:
            if self.map[country].totalCells(True) > 0:
                if self.map[country].type == "Non-Muslim":
                    if self.map[country].posture == "Hard":
                        self.map[country].printCountry()
                else:
                    if self.map[country].is_ally():
                        self.map[country].printCountry()

    def deploy_reserves(self):
        """Allows the US player to play a card for the Reserves action (6.3.3)."""
        print "Discard this card and add its Ops value to the US Reserves track."

    def show_status(self, country_name=None):
        """Shows the status of the given country, if any, otherwise the whole game."""
        if country_name:
            goodCountry = False
            possible = []
            for country in self.map:
                if country_name.lower() == country.lower():
                    possible = [country]
                    break
                elif country_name.lower() in country.lower():
                    possible.append(country)
            if len(possible) == 0:
                print "Unrecognized country."
                print ""
            elif len(possible) > 1:
                print "Be more specific", possible
                print ""
            else:
                goodCountry = possible[0]

            if goodCountry:
                self.map[goodCountry].printCountry()
                return
            else:
                return

        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
            elif self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        print ""
        print "GOOD GOVERNANCE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_good():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "FAIR GOVERNANCE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_fair():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "POOR GOVERNANCE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_poor():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "ISLAMIST RULE"
        num = 0
        for country in self.map:
            if self.map[country].type != "Non-Muslim" and self.map[country].is_islamist_rule():
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""

        # 20150131PS Start

        print "UNTESTED WITH DATA"
        num = 0
        for country in self.map:
            if self.map[country].is_ungoverned() \
                    and (self.map[country].troopCubes != 0 \
                                 or self.map[country].activeCells != 0 \
                                 or self.map[country].sleeperCells != 0 \
                                 or self.map[country].aid != 0 \
                                 or self.map[country].besieged != 0 \
                                 or self.map[country].regimeChange != 0 \
                                 or self.map[country].cadre != 0 \
                                 or self.map[country].plots != 0 \
                                 or len(self.map[country].markers) != 0 ):
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""

        # 20150131PS End

        print "HARD POSTURE"
        num = 0
        for country in self.map:
            if self.map[country].posture == "Hard":
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "SOFT POSTURE"
        num = 0
        for country in self.map:
            if self.map[country].posture == "Soft":
                num += 1
                self.map[country].printCountry()
        if not num:
            print "none"
        print ""
        print "PLOTS"
        plotCountries = 0
        for country in self.map:
            if self.map[country].plots > 0:
                plotCountries += 1
                print "%s: %d plot(s)" % (country, self.map[country].plots)
        if plotCountries == 0:
            print "No Plots"
        print ""
        print "VICTORY"
        print "Good Resources:     %d" % goodRes
        print "Islamist Resources: %d" % islamRes
        print "---"
        print "Good/Fair Countries:     %d" % goodC
        print "Poor/Islamist Countries: %d" % islamC
        print ""
        print "GWOT"
        print "US Posture: %s" % self.map["United States"].posture
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        print "World Posture: %s %d" % (worldPosStr, abs(worldPos))
        print "US Prestige: %d" % self.prestige
        print ""
        print "TROOPS"
        if self.troops >= 10:
            print "Low Intensity: %d troops available" % self.troops
        elif self.troops >= 5:
            print "War: %d troops available" % self.troops
        else:
            print "Overstretch: %d troops available" % self.troops
        print ""
        print "JIHADIST FUNDING"
        print "Funding: %d" % self.funding
        print "Cells Available: %d" % self.cells
        print ""
        print "EVENTS"
        if len(self.markers) == 0:
            print "Markers: None"
        else:
            print "Markers: %s" % ", ".join(self.markers)
        if len(self.lapsing) == 0:
            print "Lapsing: None"
        else:
            print "Lapsing: %s" % ", ".join(self.lapsing)
        print ""
        print "DATE"
        print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
        print ""

    def show_summary(self):
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
            elif self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        print ""
        print "Jihadist Ideology:", self.ideology.name
        print ""
        print "VICTORY"
        print "Good Resources: %d        Islamist Resources: %d" % (goodRes, islamRes)
        print "Good/Fair Countries: %d   Poor/Islamist Countries: %d" % (goodC, islamC)
        print ""
        if worldPos > 0:
            worldPosStr = "Hard"
        elif worldPos < 0:
            worldPosStr = "Soft"
        else:
            worldPosStr = "Even"
        print "GWOT"
        print "US Posture: %s    World Posture: %s %d" % (self.map["United States"].posture, worldPosStr, abs(worldPos))
        print "US Prestige: %d" % self.prestige
        print ""
        print "TROOPS"
        if self.troops >= 10:
            print "Low Intensity: %d troops available" % self.troops
        elif self.troops >= 5:
            print "War: %d troops available" % self.troops
        else:
            print "Overstretch: %d troops available" % self.troops
        print ""
        print "JIHADIST FUNDING"
        print "Funding: %d    Cells Available: %d" % (self.funding, self.cells)
        print ""
        print "EVENTS"
        if not self.markers:
            print "Markers: None"
        else:
            print "Markers: %s" % ", ".join(self.markers)
        if not self.lapsing:
            print "Lapsing: None"
        else:
            print "Lapsing: %s" % ", ".join(self.lapsing)
        print ""

    def _find_countries(self, predicate):
        """Returns a list of countries matching the given predicate"""
        return Utils.find(self.map.values(), predicate)

    def getAdjustFromUser(self):
        while True:
            input_str = self.my_raw_input("Enter 'ideology', 'prestige', 'funding', 'lapsing', 'marker' or country ?: ")
            if input_str == "":
                return ""
            if "ideology".startswith(input_str.lower()):
                return "ideology"
            if "prestige".startswith(input_str.lower()):
                return "prestige"
            if "funding".startswith(input_str.lower()):
                return "funding"
            if "lapsing".startswith(input_str.lower()):
                return "lapsing"
            if "marker".startswith(input_str.lower()):
                return "marker"
            possible = []
            for country in self.map:
                if input_str.lower() == country.lower():
                    possible = [country]
                    break
                elif input_str.lower() in country.lower():
                    possible.append(country)
            if len(possible) == 0:
                print "Unrecognized response."
                print ""
            elif len(possible) > 1:
                print "Be more specific", possible
                print ""
            else:
                return possible[0]

    def getAdjustIdeology(self):
        while True:
            print "Possible ideologies are:"
            for (index, ideology) in enumerate(IDEOLOGIES):
                print "(%d) %s (%s)" % (index, ideology.name, ideology.difference())
            input_str = self.my_raw_input("Enter new ideology (1-%d): " % len(IDEOLOGIES))
            if input_str == "":
                return ""
            try:
                input_int = int(input_str)
                if input_int < 1 or input_int > len(IDEOLOGIES):
                    print "Invalid ideology number '%d'" % input_int
                else:
                    return input_int
            except ValueError:
                print "Invalid ideology number '%s'" % input_str

    def adjustIdeology(self):
        print "Adjusting ideology"
        new_ideology_number = self.getAdjustIdeology()
        if new_ideology_number:
            self.ideology = get_ideology(new_ideology_number)
        else:
            print "Ideology unchanged"

    def getAdjustPrestige(self):
        while True:
            prestige_str = self.my_raw_input("Enter new prestige (1-12): ")
            if prestige_str == "":
                return ""
            try:
                prestige = int(prestige_str)
                if prestige < 1 or prestige > 12:
                    print "Invalid prestige value -", prestige
                else:
                    return prestige
            except ValueError:
                print "Invalid prestige value -", prestige_str

    def adjustPrestige(self):
        print "Adjusting prestige"
        adjustPrestigeResp = self.getAdjustPrestige()
        if adjustPrestigeResp:
            self.changePrestige(adjustPrestigeResp - self.prestige)
        else:
            print "Prestige unchanged"

    def getAdjustFunding(self):
        while True:
            funding_str = self.my_raw_input("Enter new funding (1-9): ")
            if funding_str == "":
                return ""
            try:
                funding = int(funding_str)
                if funding < 1 or funding > 9:
                    print "Invalid funding value -", funding
                else:
                    return funding
            except ValueError:
                print "Invalid funding value -", funding_str

    def adjustFunding(self):
        print "Adjusting funding"
        adjustFundResp = self.getAdjustFunding()
        if adjustFundResp:
            self.changeFunding(adjustFundResp - self.funding)
        else:
            print "Funding unchanged"

    def adjustLapsing(self):
        print "Adjusting lapsing event"
        if len(self.lapsing) == 0:
            print "There are no lapsing events"
        else:
            print "Current lapsing events: %s" % ", ".join(self.lapsing)
        print ""
        print "Available lapsing events are:"
        for validEvent in self.validLapsingMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it:"
        while True:
            event = self.my_raw_input("Enter event to be added or removed: ")
            if event == "":
                return ""
            if event in self.lapsing:
                self.lapsing.remove(event)
                print "Removed lapsing event -", event
                break
            elif event in self.validLapsingMarkers:
                self.lapsing.append(event)
                print "Added lapsing event -", event
                break
            else:
                print "Not a valid event"
        if len(self.lapsing) == 0:
            print "There are now no lapsing events"
        else:
            print "Current lapsing events: %s" % ", ".join(self.lapsing)
        print ""

    def adjustMarker(self):
        print "Adjusting event markers in play"
        if len(self.markers) == 0:
            print "There are no event markers in play"
        else:
            print "Current events in play: %s" % ", ".join(self.markers)
        print ""
        print "Available global events are:"
        for validEvent in self.validGlobalMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it"
        while True:
            event = self.my_raw_input("Enter event to be added or removed: ")
            if event == "":
                return ""
            if event in self.markers:
                self.markers.remove(event)
                print "Removed event -", event
                break
            elif event in self.validGlobalMarkers:
                self.markers.append(event)
                print "Added event -", event
                break
            else:
                print "Not a valid event"
        if len(self.markers) == 0:
            print "There are now no events in play"
        else:
            print "Current events in play: %s" % ", ".join(self.markers)
        print ""

    def adjustCountryGovernance(self, country):
        print "Adjusting governance for -", country
        while True:
            gov_str = self.my_raw_input("Enter governance (0-4) (0 = untested): ")
            if gov_str == "":
                return False
            try:
                gov_num = int(gov_str)
                self.map[country].make_governance(governance_with_level(gov_num))
                print "Changing governance to", gov_num
                return True
            except ValueError:
                print "Invalid governance value -", gov_str

    def adjustCountryAlignment(self, country):
        print "Adjusting alignment for -", country
        while True:
            alignment = self.my_raw_input("Enter alignment ('Ally', 'Neutral', 'Adversary'): ")
            if alignment == "":
                return False
            if alignment == "Adversary":
                print "Changing alignment to Adversary"
                self.map[country].make_adversary()
                return True
            if alignment == "Ally":
                print "Changing alignment to Ally"
                self.map[country].make_ally()
                return True
            if alignment == "Neutral":
                print "Changing alignment to Neutral"
                self.map[country].make_neutral()
                return True
            print "Invalid alignment value -", alignment

    def adjustCountryPosture(self, country):
        """Prompts the user to set the posture of the given country (returns true if successful)"""
        print "Adjusting posture for -", country
        while True:
            posture = self.my_raw_input("Enter posture ('Hard', 'Soft', 'Untested'): ")
            if posture == "":  # User aborted
                return False
            if posture.lower() == "hard":
                print "Changing posture to Hard"
                self.map[country].make_hard()
                return True
            if posture.lower() == "soft":
                print "Changing posture to Soft"
                self.map[country].make_soft()
                return True
            if posture.lower() == "untested":
                print "Changing posture to Untested"
                self.map[country].remove_posture()
                return True
            print "Invalid posture value '{}'".format(posture)
            return False

    def adjustCountryTroops(self, country):
        print "Adjusting troops for - ", country
        if 'NATO' in self.map[country].markers:
            print "NATO contributes 2 troops to count, actual troop cubes are ", self.map[country].troopcubes
        while True:
            troop_str = self.my_raw_input("Enter new troop count (0-15): ")
            if troop_str == "":
                return False
            try:
                troops = int(troop_str)
                if troops < 0 or troops > 15:
                    print "Invalid troop cube value -", troops
                else:
                    print "Changing troop cubes to", troops
                    troopChange = troops - self.map[country].troopCubes
                    self.troops -= troopChange
                    self.map[country].troopCubes = troops
                    if self.troops < 0 or self.troops > 15:
                        print "WARNING! Troop track count is now ", self.troops
                    else:
                        print "Troop track count is now ", self.troops
                    return True
            except ValueError:
                print "Invalid troop cube value -", troop_str

    def adjustCountryActive(self, country):
        print "Adjusting active cells for - ", country
        while True:
            cell_str = self.my_raw_input("Enter new active cell count (0-15): ")
            if cell_str == "":
                return False
            try:
                cells = int(cell_str)
                if cells < 0 or cells > 15:
                    print "Invalid active cell value -", cells
                else:
                    print "Changing active cells to ", cells
                    activeChange = cells - self.map[country].activeCells
                    self.cells -= activeChange
                    self.map[country].activeCells = cells
                    if self.cells < 0 or self.cells > 15:
                        print "WARNING! Cell count on funding track is now ", self.cells
                    else:
                        print "Cell count on funding track is now ", self.cells
                    return True
            except ValueError:
                print "Invalid active cell value -", cell_str

    def adjustCountrySleeper(self, country):
        print "Adjusting sleeper cells for - ", country
        while True:
            cell_str = self.my_raw_input("Enter new sleeper cell count (0-15): ")
            if cell_str == "":
                return False
            try:
                cells = int(cell_str)
                if cells < 0 or cells > 15:
                    print "Invalid sleeper cell value -", cells
                else:
                    print "Changing sleeper cells to", cells
                    sleeperChange = cells - self.map[country].sleeperCells
                    self.cells -= sleeperChange
                    self.map[country].sleeperCells = cells
                    if self.cells < 0 or self.cells > 15:
                        print "WARNING! Cell count on funding track is now ", self.cells
                    else:
                        print "Cell count on funding track is now ", self.cells
                    return True
            except ValueError:
                print "Invalid sleeper cell value -", cell_str

    def adjustCountryCadre(self, country):
        print "Adjusting cadre for - ", country
        while True:
            cadre_str = self.my_raw_input("Enter new cadre count (0-1): ")
            if cadre_str == "":
                return False
            try:
                cadres = int(cadre_str)
                if cadres < 0 or cadres > 1:
                    print "Invalid cadre value -", cadres
                else:
                    print "Changing cadre count to", cadres
                    self.map[country].cadre = cadres
                    return True
            except ValueError:
                print "Invalid cadre value -", cadre_str

    def adjustCountryAid(self, country):
        print "Adjusting aid for - ", country
        while True:
            aid_str = self.my_raw_input("Enter new aid count (0-9): ")
            if aid_str == "":
                return False
            try:
                aid = int(aid_str)
                if aid < 0 or aid > 9:
                    print "Invalid aid value -", aid
                else:
                    print "Changing aid count to", aid
                    self.map[country].aid = aid
                    return True
            except:
                print "Invalid aid value -", aid_str

    def adjustCountryBesieged(self, country):
        print "Adjusting besieged for - ", country
        while True:
            input = self.my_raw_input("Enter new besieged count (0-1): ")
            if input == "":
                return False
            try:
                input = int(input)
                if input < 0 or input > 1:
                    print "Invalid besieged value - ", input
                else:
                    print "Changing besieged count to ", input
                    self.map[country].besieged = input
                    return True
            except:
                print "Invalid besieged value - ", input

    def adjustCountryRegime(self, country):
        print "Adjusting regime change for - ", country
        while True:
            input = self.my_raw_input("Enter new regime change count (0-1): ")
            if input == "":
                return False
            try:
                input = int(input)
                if input < 0 or input > 1:
                    print "Invalid regime change value - ", input
                else:
                    print "Changing regime change count to ", input
                    self.map[country].regimeChange = input
                    return True
            except:
                print "Invalid regime change value - ", input

    def adjustCountryPlots(self, country):
        print "Adjusting plots for - ", country
        while True:
            input = self.my_raw_input("Enter new plot count (0-9): ")
            if input == "":
                return False
            try:
                input = int(input)
                if input < 0 or input > 9:
                    print "Invalid plot value - ", input
                else:
                    print "Changing plot count to", input
                    self.map[country].plots = input
                    return True
            except:
                print "Invalid plot value - ", input

    def adjustCountryMarker(self, country):
        print "Adjusting event markers for - ", country
        if len(self.map[country].markers) == 0:
            print "There are no event markers in play"
        else:
            print "Current events in play: %s" % ", ".join(self.map[country].markers)
        print ""
        print "Available country events are:"
        for validEvent in self.validCountryMarkers:
            print validEvent
        print "Enter a new event to add it to the list or enter an existing event to remove it"
        while True:
            input = self.my_raw_input("Enter event to be added or removed: ")
            if input == "":
                return ""
            if input in self.map[country].markers:
                self.map[country].markers.remove(input)
                print "Removed event - ", input
                break
            elif input in self.validCountryMarkers:
                self.map[country].markers.append(input)
                print "Added event - ", input
                break
            else:
                print "Not a valid event"
        if len(self.map[country].markers) == 0:
            print "There are now no events in play"
        else:
            print "Current events in play: %s" % ", ".join(self.map[country].markers)
        print ""
        return True

    def adjustCountry(self, country):
        print "Adjusting country - ", country
        self.map[country].printCountry()
        if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
            adjustAttrList = "governance", "alignment", "troops", "active", "sleeper", "cadre", "aid", "besieged", "regime", "plots", "marker"
        elif self.map[country].name == "Philippines":
            adjustAttrList = "posture", "troops", "active", "sleeper", "cadre", "plots", "marker"
        elif self.map[country].type == "Non-Muslim":
            adjustAttrList = "posture", "active", "sleeper", "cadre", "plots", "marker"
        elif self.map[country].type == "Iran":
            adjustAttrList =  "active", "sleeper", "cadre", "plots", "marker"
        goodAdjustAttr = None
        while not goodAdjustAttr:
            print "Changeable attributes are: %s" % ", ".join(adjustAttrList)
            input = self.my_raw_input("Enter attribute to be changed (press Enter to quit): ")
            if input == "":
                return ""
            if input in adjustAttrList:
                adjustSuccess = False
                if input == "governance":
                    adjustSuccess = self.adjustCountryGovernance(country)
                elif input == "alignment":
                    adjustSuccess = self.adjustCountryAlignment(country)
                elif input == "posture":
                    adjustSuccess = self.adjustCountryPosture(country)
                elif input == "troops":
                    adjustSuccess = self.adjustCountryTroops(country)
                elif input == "active":
                    adjustSuccess = self.adjustCountryActive(country)
                elif input == "sleeper":
                    adjustSuccess = self.adjustCountrySleeper(country)
                elif input == "cadre":
                    adjustSuccess = self.adjustCountryCadre(country)
                elif input == "aid":
                    adjustSuccess = self.adjustCountryAid(country)
                elif input == "besieged":
                    adjustSuccess = self.adjustCountryBesieged(country)
                elif input == "regime":
                    adjustSuccess = self.adjustCountryRegime(country)
                elif input == "plots":
                    adjustSuccess = self.adjustCountryPlots(country)
                elif input == "marker":
                    adjustSuccess = self.adjustCountryMarker(country)
                if adjustSuccess:
                    self.map[country].printCountry()
                else:
                    print country, "unchanged"
            else:
                print "Invalid attribute - ", input

    def adjust_state(self):
        print "Warning! No cross validation of data changes is carried out"
        print "Start adjusting"
        adjustType = self.getAdjustFromUser()
        if adjustType == "":
            print ""
            return
        elif adjustType == "ideology":
            self.adjustIdeology()
        elif adjustType == "prestige":
            self.adjustPrestige()
        elif adjustType == "funding":
            self.adjustFunding()
        elif adjustType == "lapsing":
            self.adjustLapsing()
        elif adjustType == "marker":
            self.adjustMarker()
        else:
            self.adjustCountry(adjustType)
        print ""

    def show_history(self, argument):
        if argument == 'save':
            f = open('history.txt','w')
            for event in self.history:
                f.write(event + "\r\n")
            f.close()
        for event in self.history:
            print event
        print ""

    def deploy_troops(self):
        """Deploys troops to a Muslim Ally; does not perform Regime Change"""
        if not self._find_countries(lambda c: self._can_deploy_to(c.name)):
            print "There are no Muslim Allies to deploy to."
            return
        moveFrom = None
        available = 0
        while not moveFrom:
            input = self.getCountryFromUser("From what country (track for Troop Track) (? for list)?: ",  "track", self.listCountriesWithTroops)
            if input == "":
                print ""
                return
            elif input == "track":
                if self.troops <= 0:
                    print "There are no troops on the Troop Track."
                    print ""
                    return
                else:
                    print "Deploy from Troop Track - %d available" % self.troops
                    print ""
                    available = self.troops
                    moveFrom = input
            else:
                if self.map[input].troops() <= 0:
                    print "There are no troops in %s." % input
                    print ""
                    return
                else:
                    print "Deploy from %s = %d available" % (input, self.map[input].troops())
                    print ""
                    available = self.map[input].troops()
                    moveFrom = input
        moveTo = None
        while not moveTo:
            input = self.getCountryFromUser(
                "To what country ('track' for Troop Track, ? for list): ", "track", self.listDeployOptions)
            if input == "":
                print ""
                return
            elif input == "track":
                print "Deploying troops from %s to Troop Track" % moveFrom
                print ""
                moveTo = input
            else:
                print "Deploying troops from %s to %s" % (moveFrom, input)
                print ""
                moveTo = input
        howMany = 0
        while not howMany:
            input = self.getNumTroopsFromUser("Deploy how many troops (%d available)? " % available, available)
            if input == "":
                print ""
                return
            else:
                howMany = input
        if moveFrom == "track":
            self.troops -= howMany
            troopsLeft = self.troops
        else:
            if self.map[moveFrom].regimeChange:
                if (self.map[moveFrom].troops() - howMany) < (5 + self.map[moveFrom].totalCells(True)):
                    print "You cannot move that many troops from a Regime Change country."
                    print ""
                    return
            self.map[moveFrom].changeTroops(-howMany)
            troopsLeft = self.map[moveFrom].troops()
        if moveTo == "track":
            self.troops += howMany
            troopsNow = self.troops
        else:
            self.map[moveTo].changeTroops(howMany)
            troopsNow = self.map[moveTo].troops()
        self.outputToHistory(
            "* %d troops deployed from %s (%d) to %s (%d)" % (howMany, moveFrom, troopsLeft, moveTo, troopsNow))

    def disrupt_cells_or_cadre(self):
        """Performs a Disrupt operation for the US player."""
        if not self._find_countries(lambda c: c.can_disrupt()):
            print "No countries can be disrupted."
            return
        where = None
        sleepers = 0
        actives = 0
        while not where:
            input = self.getCountryFromUser("Disrupt what country?  (? for list): ",  "XXX", self.listDisruptableCountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].sleeperCells + self.map[input].activeCells <= 0 and self.map[input].cadre <= 0:
                    print "There are no cells or cadre in %s." % input
                    print ""
                elif "FATA" in self.map[input].markers and self.map[input].regimeChange == 0:
                    print "No disrupt allowed due to FATA."
                    print ""
                elif self.map[input].troops() > 0 or self.map[input].type == "Non-Muslim" or self.map[input].is_ally():
                    print ""
                    where = input
                    sleepers = self.map[input].sleeperCells
                    actives = self.map[input].activeCells
                else:
                    print "You can't disrupt there."
                    print ""
        self.handleDisrupt(where)

    def war_of_ideas(self):
        where = None
        while not where:
            input = self.getCountryFromUser("War of Ideas in what country?  (? for list): ", "XXX", self.listWoICountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].type == "Non-Muslim" and input != "United States":
                    where = input
                elif self.map[input].is_ally() or self.map[input].is_neutral() or self.map[input].is_ungoverned():
                    where = input
                else:
                    print "Country not eligible for War of Ideas."
                    print ""
        if self.map[where].type == "Non-Muslim" and input != "United States":  # Non-Muslim
            postureRoll = self.getRollFromUser("Enter Posture Roll or r to have program roll: ")
            if postureRoll > 4:
                self.map[where].posture = "Hard"
                self.outputToHistory("* War of Ideas in %s - Posture Hard" % where)
                if self.map["United States"].posture == "Hard":
                    self._increase_prestige(1)
                    self.outputToHistory("US Prestige now %d" % self.prestige)
            else:
                self.map[where].posture = "Soft"
                self.outputToHistory("* War of Ideas in %s - Posture Soft" % where)
                if self.map["United States"].posture == "Soft":
                    self._increase_prestige(1)
                    self.outputToHistory("US Prestige now %d" % self.prestige)
        else:  # Muslim
            self.testCountry(where)
            woiRoll = self.getRollFromUser("Enter WoI roll or r to have program roll: ")
            modRoll = self.modifiedWoIRoll(woiRoll, where)
            self.outputToHistory("Modified Roll: %d" % modRoll)
            self.handleMuslimWoI(modRoll, where)

    def alert_plot(self):
        if not self._find_countries(lambda c: c.plots > 0):
            print "No countries contain plots."
            return
        where = None
        alert_prompt = "Alert in what country?  (? for list, Enter to abort): "
        while not where:
            input = self.getCountryFromUser(alert_prompt, "XXX", self.listPlotCountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].plots < 1:
                    print "Country has no plots."
                    print ""
                else:
                    where = input
        self.handleAlert(where)

    def change_regime(self):
        if self.map["United States"].posture == "Soft":
            print "No Regime Change with US Posture Soft"
            print ""
            return
        where = None
        while not where:
            input = self.getCountryFromUser("Regime Change in what country?  (? for list): ", "XXX", self.listIslamistCountries)
            if input == "":
                print ""
                return
            else:
                if (self.map[input].is_islamist_rule()) or (input == "Iraq" and "Iraqi WMD" in self.markers) or (input == "Libya" and "Libyan WMD" in self.markers):
                    where = input
                else:
                    print "Country not Islamist Rule."
                    print ""
        moveFrom = None
        available = 0
        while not moveFrom:
            input = self.getCountryFromUser("Deploy 6+ troops from what country (track for Troop Track) (? for list)?: ",  "track", self.listCountriesWithTroops, 6)
            if input == "":
                print ""
                return
            elif input == "track":
                if self.troops <= 6:
                    print "There are not enough troops on the Troop Track."
                    print ""
                    return
                else:
                    print "Deploy from Troop Track - %d available" % self.troops
                    print ""
                    available = self.troops
                    moveFrom = input
            else:
                if self.map[input].troops() <= 6:
                    print "There are not enough troops in %s." % input
                    print ""
                    return
                else:
                    print "Deploy from %s = %d available" % (input, self.map[input].troops())
                    print ""
                    available = self.map[input].troops()
                    moveFrom = input
        howMany = 0
        while not howMany:
            input = self.getNumTroopsFromUser("Deploy how many troops (%d available)? " % available, available)
            if input == "":
                print ""
                return
            elif input < 6:
                print "At least 6 troops needed for Regime Change"
            else:
                howMany = input
        govRoll = self.getRollFromUser("Enter Governance roll or r to have program roll: ")
        preFirstRoll = self.getRollFromUser("Enter first die (Raise/Drop) for Prestige roll or r to have program roll: ")
        preSecondRoll = self.getRollFromUser("Enter second die for Prestige roll or r to have program roll: ")
        preThirdRoll = self.getRollFromUser("Enter third die for Prestige roll or r to have program roll: ")
        self.handleRegimeChange(where, moveFrom, howMany, govRoll, (preFirstRoll, preSecondRoll, preThirdRoll))

    def withdraw_troops(self):
        if self.map["United States"].posture == "Hard":
            print "No Withdrawal with US Posture Hard"
            print ""
            return
        moveFrom = None
        available = 0
        while not moveFrom:
            input = self.getCountryFromUser("Withdrawal in what country?  (? for list): ", "XXX", self.listRegimeChangeCountries)
            if input == "":
                print ""
                return
            else:
                if self.map[input].regimeChange > 0:
                    moveFrom = input
                    available = self.map[input].troops()
                else:
                    print "Country not Regime Change."
                    print ""
        moveTo = None
        while not moveTo:
            input = self.getCountryFromUser("To what country (track for Troop Track)  (? for list)?: ",  "track", self.listDeployOptions)
            if input == "":
                print ""
                return
            elif input == "track":
                print "Withdraw troops from %s to Troop Track" % moveFrom
                print ""
                moveTo = input
            else:
                print "Withdraw troops from %s to %s" % (moveFrom, input)
                print ""
                moveTo = input
        howMany = 0
        while not howMany:
            input = self.getNumTroopsFromUser("Withdraw how many troops (%d available)? " % available, available)
            if input == "":
                print ""
                return
            else:
                howMany = input
        preFirstRoll = self.getRollFromUser("Enter first die (Raise/Drop) for Prestige roll or r to have program roll: ")
        preSecondRoll = self.getRollFromUser("Enter second die for Prestige roll or r to have program roll: ")
        preThirdRoll = self.getRollFromUser("Enter third die for Prestige roll or r to have program roll: ")
        self.handleWithdraw(moveFrom, moveTo, howMany, (preFirstRoll, preSecondRoll, preThirdRoll))

    def play_jihadist_card(self, card_num_str):
        card_num = self._parse_card_number(card_num_str)
        if not card_num:
            return
        self.SaveUndo()
        self.outputToHistory("", False)
        self.outputToHistory("== Jihadist plays %s - %d Ops ==" % (self.deck[str(card_num)].name, self.deck[str(card_num)].ops), True)
        self.aiFlowChartTop(card_num)

    @staticmethod
    def _parse_card_number(card_num_str):
        try:
            card_num = int(card_num_str)
            if card_num < 1 or card_num > 120:
                print "Enter a card number from 1 to 120"
                print ""
                return None
            else:
                return card_num
        except ValueError:
            print "Enter a card number from 1 to 120"
            print ""
            return None

    def play_us_card(self, card_num_str):
        """Plays the given card as the US when it's the US action phase."""
        card_num = self._parse_card_number(card_num_str)
        if not card_num:
            return
        self.SaveUndo()
        self.outputToHistory("", False)
        self.outputToHistory("== US plays %s - %d Ops ==" % (self.deck[str(card_num)].name, self.deck[str(card_num)].ops), True)

        if self.deck[str(card_num)].playable("US", self, True):
            self.outputToHistory("Playable %s Event" % self.deck[str(card_num)].type, False)
            if card_num != 120:
                choice = self.getEventOrOpsFromUser("Play card for Event or Ops (enter e or o): ")
            else:
                choice = self.getEventOrOpsFromUser("This event must be played, do you want the Event or Ops to happen first (enter e or o): ")
            if choice == "event":
                self.outputToHistory("Played for Event.", False)
                self.deck[str(card_num)].playEvent("US", self)
                if card_num == 120:
                    print "Now, %d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(card_num)].ops
            elif choice == "ops":
                self.outputToHistory("Played for Ops.", False)
                if card_num == 120:
                    print "When finished with Ops enter u 120 again to play the event."
                print "%d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(card_num)].ops
        else:
            if self.deck[str(card_num)].type == "Jihadist":
                if self.deck[str(card_num)].playable("Jihadist", self, True):
                    self.outputToHistory("Jihadist Event is playable.", False)
                    playEventFirst = self.getYesNoFromUser("Do you want to play the Jihadist event before using the Ops? (y/n): ")
                    if playEventFirst:
                        self.deck[str(card_num)].playEvent("Jihadist", self)
                    else:
                        print "Use the Ops now then enter u <card #> again to play the event"
                    print "%d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(card_num)].ops
                    return
                    # Here if it's unplayable by either side.
            self.outputToHistory("Unplayable %s Event" % self.deck[str(card_num)].type, False)
            print "%d Ops available. Use commands: alert, deploy, disrupt, reassessment, regime, withdraw, or woi" % self.deck[str(card_num)].ops

    def resolve_plots(self):
        """Resolves any active plots at the end of the US action phase."""
        foundPlot = False
        for country in self.map:
            while self.map[country].plots > 0:
                if not foundPlot:
                    self.outputToHistory("", False)
                    self.outputToHistory("[[ Resolving Plots ]]", True)
                foundPlot = True
                print ""
                plotType = self.getPlotTypeFromUser("Enter Plot type from %s: " % country)
                print ""
                isBacklash = False
                if self.backlashInPlay and (self.map[country].type != 'Non-Muslim'):
                    isBacklash = self.getYesNoFromUser("Was this plot selected with backlash (y/n): ")
                postureRoll = 0
                usPrestigeRolls = []
                schCountries = []
                schPostureRolls = []
                govRolls = []
                if country == "United States":
                    if plotType != "WMD":
                        postureRoll = random.randint(1, 6)
                        usPrestigeRolls.append(random.randint(1, 6))
                        usPrestigeRolls.append(random.randint(1, 6))
                        usPrestigeRolls.append(random.randint(1, 6))
                elif self.map[country].type != "Non-Muslim":
                    if country != "Iran":
                        numRolls = 0
                        if plotType == "WMD":
                            numRolls = 3
                        else:
                            numRolls = plotType
                        for i in range(numRolls):
                            govRolls.append(random.randint(1, 6))
                elif self.map[country].type == "Non-Muslim":
                    postureRoll = random.randint(1, 6)
                    if self.map[country].schengen:
                        schChoices = []
                        for cou in self.map:
                            if cou != country and self.map[cou].schengen:
                                schChoices.append(cou)
                        schCountries.append(random.choice(schChoices))
                        schCountries.append(schCountries[0])
                        while schCountries[0] == schCountries[1]:
                            schCountries[1] = random.choice(schChoices)
                        for i in range(2):
                            schPostureRolls.append(random.randint(1, 6))
                self.resolvePlot(country, plotType, postureRoll, usPrestigeRolls, schCountries, schPostureRolls, govRolls, isBacklash)
        if not foundPlot:
            self.outputToHistory("", False)
            self.outputToHistory("[[ No unblocked plots to resolve ]]", True)
        self.backlashInPlay = False

    def end_turn(self):
        """Performs end-of-turn activities."""
        self.saver.save_turn_file(self)

        self.outputToHistory("* End of Turn.", False)
        if "Pirates" in self.markers and (self.map["Somalia"].is_islamist_rule() or self.map["Yemen"].is_islamist_rule()):
            self.outputToHistory("No funding drop due to Pirates.", False)
        else:
            self.funding -= 1
            if self.funding < 1:
                self.funding = 1
            self.outputToHistory("Jihadist Funding now %d" % self.funding, False)
        anyIR = False
        for country in self.map:
            if self.map[country].is_islamist_rule():
                anyIR = True
                break
        if anyIR:
            self._reduce_prestige(1)
            self.outputToHistory("Islamist Rule - US Prestige now %d" % self.prestige, False)
        else:
            self.outputToHistory("No Islamist Rule - US Prestige stays at %d" % self.prestige, False)  # 20150131PS - added
        worldPos = 0
        for country in self.map:
            if not (self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni") and self.map[country].type != "Iran" and self.map[country].name != "United States":
                if self.map[country].posture == "Hard":
                    worldPos += 1
                elif self.map[country].posture == "Soft":
                    worldPos -= 1
        if (self.map["United States"].posture == "Hard" and worldPos >= 3) or (self.map["United States"].posture == "Soft" and worldPos <= -3):
            self._increase_prestige(1)
            self.outputToHistory("GWOT World posture is 3 and matches US - US Prestige now %d" % self.prestige, False)
        for event in self.lapsing:
            self.outputToHistory("%s has Lapsed." % event, False)
        self.lapsing = []
        goodRes = 0
        islamRes = 0
        goodC = 0
        islamC = 0
        worldPos = 0
        for country in self.map:
            if self.map[country].type == "Shia-Mix" or self.map[country].type == "Suni":
                if self.map[country].is_good():
                    goodC += 1
                    goodRes += self.countryResources(country)
                elif self.map[country].is_fair():
                    goodC += 1
                elif self.map[country].is_poor():
                    islamC += 1
                elif self.map[country].is_islamist_rule():
                    islamC += 1
                    islamRes += self.countryResources(country)
        self.outputToHistory("---", False)
        self.outputToHistory("Good Resources:     %d" % goodRes, False)
        self.outputToHistory("Islamist Resources: %d" % islamRes, False)
        self.outputToHistory("---", False)
        self.outputToHistory("Good/Fair Countries:     %d" % goodC, False)
        self.outputToHistory("Poor/Islamist Countries: %d" % islamC, False)
        self.turn += 1
        self.outputToHistory("---", False)
        self.outputToHistory("", False)
        usCards = 0
        jihadistCards = 0
        if self.funding >= 7:
            jihadistCards = 9
        elif self.funding >= 4:
            jihadistCards = 8
        else:
            jihadistCards = 7
        if self.troops >= 10:
            usCards = 9
        elif self.troops >= 5:
            usCards = 8
        else:
            usCards = 7
        self.outputToHistory("Jihadist draws %d cards." % jihadistCards, False)
        self.outputToHistory("US draws %d cards." % usCards, False)
        self.outputToHistory("---", False)
        self.outputToHistory("", False)
        self.outputToHistory("[[ %d (Turn %s) ]]" % (self.startYear + (self.turn - 1), self.turn), False)

    def undo_last_turn(self):
        self.undo = self.getYesNoFromUser("Undo to last card played? (y/n): ")

    def quit(self):
        if self.getYesNoFromUser("Save? (y/n): "):
            print "Saving suspend file."
            self.saver.save_suspend_file(self)
        print "Exiting."

    def print_turn_number(self):
        print "%d (Turn %s)" % (self.startYear + (self.turn - 1), self.turn)
        print ""

    def SaveUndo(self):
        """Saves the undo file for this game"""
        self.saver.save_undo_file(self)

    def roll_back(self):
        self.roll_turn = -1
        needTurn = True
        while needTurn:
            try:
                last_turn = self.turn - 1
                turn_str = raw_input("Roll back to which turn? (0 to %d, or Q to cancel): " % last_turn)
                if turn_str.upper() == "Q":
                    print "Rollback cancelled"
                    break
                else:
                    turn_number = int(turn_str)
                    if 0 <= turn_number <= last_turn:
                        self.roll_turn = turn_number
                        needTurn = False
                    else:
                        raise ValueError
            except ValueError:
                print "Entry error"
                print ""
