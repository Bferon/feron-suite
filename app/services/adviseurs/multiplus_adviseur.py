from app.models.ess_wizard import EssWizard
from app.data.victron_producten import MULTIPLUS


class MultiPlusAdviseur:

    def __init__(self, ess: EssWizard):
        self.ess = ess

    def bepaal(self):

        # Alleen 1-fase in versie 1.0
        if self.ess.netaansluiting == "1-fase":

            if self.ess.hoofdzekering <= 25:
                return MULTIPLUS["48/3000"]

            elif self.ess.hoofdzekering <= 35:
                return MULTIPLUS["48/5000"]

            else:
                return MULTIPLUS["48/8000"]

        # 3-fase ondersteuning volgt later
        return None