from typing import Dict


def analyseer_werkzaamheden(omschrijving: str) -> Dict:

    resultaat = {
        "werkzaamheden": [],
        "materialen": [],
        "arbeid": "",
        "prijs": "",
        "advies": [],
    }

    tekst = omschrijving.lower()

    # ESS
    if "ess" in tekst:
        resultaat["werkzaamheden"].append("ESS-installatie plaatsen")

    # Meterkast
    if "groepenkast" in tekst:
        resultaat["werkzaamheden"].append("Groepenkast vervangen")

    # Laadpaal
    if "laadpaal" in tekst:
        resultaat["werkzaamheden"].append("Laadpaal installeren")

    # Schneider
    if "schneider" in tekst:
        resultaat["materialen"].append("Schneider componenten")

    # Victron
    if "victron" in tekst:
        resultaat["materialen"].append("Victron apparatuur")

    # Dyness
    if "dyness" in tekst:
        resultaat["materialen"].append("Dyness accu")

    resultaat["arbeid"] = "Nog te berekenen"

    resultaat["prijs"] = "Nog te berekenen"

    resultaat["advies"].append(
        "OpenAI AI-koppeling volgt in de volgende stap."
    )

    return resultaat