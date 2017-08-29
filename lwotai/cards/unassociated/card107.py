import random

from lwotai.cards.unassociated.unassociated_card import UnassociatedCard
from lwotai.governance import POOR


class Card107(UnassociatedCard):

    def __init__(self):
        super(Card107, self).__init__(107, "Kurdistan", 2, False, False, False, False)

    def play_event(self, side, app):
        if side == "US":
            app.test_country("Iraq")
            app.get_country("Iraq").add_aid(1)
            app.output_to_history("Aid added to Iraq.", False)
            app.output_to_history(app.get_country("Iraq").summary(), True)
        else:
            app.test_country("Turkey")
            possibles = []
            if app.get_country("Turkey").governance_is_better_than(POOR):
                possibles.append("Turkey")
            iraq = app.get_country("Iraq")
            if iraq.is_governed() and iraq.governance_is_better_than(POOR):
                possibles.append("Iraq")
            if len(possibles) == 0:
                app.output_to_history("Iraq and Turkey cannot have governance worsened.", True)
                return
            elif len(possibles) == 0:
                target_name = possibles[0]
            else:
                country_scores = {}
                for country in possibles:
                    country_scores[country] = 0
                    if app.get_country(country).get_aid() > 0:
                        country_scores[country] += 10000
                    if app.get_country(country).is_besieged():
                        country_scores[country] += 1000
                    country_scores[country] += (app.country_resources_by_name(country) * 100)
                    country_scores[country] += random.randint(1, 99)
                country_order = []
                for country in country_scores:
                    country_order.append(
                        (country_scores[country], (app.get_country(country).total_cells(True)), country))
                country_order.sort()
                country_order.reverse()
                target_name = country_order[0][2]
            app.worsen_governance(target_name)
            app.output_to_history("Governance worsened in %s." % target_name, False)
            app.output_to_history(app.get_country(target_name).summary(), True)
