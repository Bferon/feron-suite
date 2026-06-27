from app.services.adviseurs.multiplus_adviseur import MultiPlusAdviseur
from app.services.adviseurs.accu_adviseur import AccuAdviseur
from app.models.ess_wizard import EssWizard

from app.data.victron_producten import (
    MULTIPLUS,
    ACCU,
    CERBO,
    GX_TOUCH,
    ENERGIEMETER,
    LYNX,
)


class EssAdviseur:

    def __init__(self, ess: EssWizard):
        self.ess = ess

    def bepaal_multiplus(self):

    advies = MultiPlusAdviseur(self.ess).bepaal()

    if advies:
        return advies["naam"]

    return "Nog geen advies beschikbaar"

        # 1-fase
        if self.ess.netaansluiting == "1-fase":

            if self.ess.hoofdzekering <= 25:
                return MULTIPLUS["48/3000"]["naam"]

            elif self.ess.hoofdzekering <= 35:
                return MULTIPLUS["48/5000"]["naam"]

            else:
                return MULTIPLUS["48/8000"]["naam"]

        # 3-fase (tijdelijk)
        return "Victron MultiPlus-II 48/5000 (3-fase nog niet ondersteund)"

    def bepaal_accu(self):

    advies = AccuAdviseur(self.ess).bepaal()

    return advies["naam"]

        if self.ess.jaarverbruik <= 2500:
            return ACCU["10G2"]["naam"]

        elif self.ess.jaarverbruik <= 5000:
            return ACCU["14G2"]["naam"]

        else:
            return "Advies op maat"

    def bepaal_cerbo(self):
        return CERBO["naam"]

    def bepaal_gx_touch(self):
        return GX_TOUCH["naam"]

    def bepaal_energiemeter(self):
        return ENERGIEMETER["naam"]

    def bepaal_lynx(self):
        return LYNX["naam"]

    def genereer_advies(self):

        return {

            "multiplus": self.bepaal_multiplus(),

            "accu": self.bepaal_accu(),

            "cerbo": self.bepaal_cerbo(),

            "gx_touch": self.bepaal_gx_touch(),

            "energiemeter": self.bepaal_energiemeter(),

            "lynx": self.bepaal_lynx(),

        }