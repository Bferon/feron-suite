from app.models.ess_wizard import EssWizard


class EssService:

    @staticmethod
    def bepaal_multiplus(ess: EssWizard):

        if ess.netaansluiting == "1-fase":

            if ess.hoofdzekering <= 25:
                return "Victron MultiPlus-II 48/3000"

            elif ess.hoofdzekering <= 35:
                return "Victron MultiPlus-II 48/5000"

            else:
                return "Victron MultiPlus-II 48/8000"

        return "Victron MultiPlus-II 48/5000"

    @staticmethod
    def bepaal_accu(ess: EssWizard):

        if ess.jaarverbruik <= 2500:
            return "Dyness Powerbox G2 10.24 kWh"

        elif ess.jaarverbruik <= 5000:
            return "Dyness Powerbox G2 14.33 kWh"

        else:
            return "Meerdere accu's adviseren"

    @staticmethod
    def bepaal_cerbo():

        return "Cerbo GX"

    @staticmethod
    def bepaal_gx_touch():

        return "GX Touch 50"

    @staticmethod
    def genereer_advies(ess: EssWizard):

        return {
            "multiplus": EssService.bepaal_multiplus(ess),
            "accu": EssService.bepaal_accu(ess),
            "cerbo": EssService.bepaal_cerbo(),
            "gx_touch": EssService.bepaal_gx_touch(),
        }