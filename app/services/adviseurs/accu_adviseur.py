from app.models.ess_wizard import EssWizard
from app.data.victron_producten import ACCU


class AccuAdviseur:

    def __init__(self, ess: EssWizard):
        self.ess = ess

    def bepaal(self):

        score = self.bereken_benodigde_capaciteit()

        if score <= 10:
            return ACCU["10G2"]

        elif score <= 15:
            return ACCU["14G2"]

        return {
            "naam": "Advies op maat",
            "capaciteit": score,
        }

    def bereken_benodigde_capaciteit(self):

        capaciteit = 10

        # Jaarverbruik
        if self.ess.jaarverbruik > 4000:
            capaciteit += 2

        if self.ess.jaarverbruik > 6000:
            capaciteit += 3

        # Elektrische auto
        if self.ess.elektrische_auto:
            capaciteit += 4

        # Warmtepomp
        if self.ess.warmtepomp:
            capaciteit += 3

        # Airco
        if self.ess.airco:
            capaciteit += 1

        # Noodstroom
        if self.ess.noodstroom:
            capaciteit += 2

        return capaciteit