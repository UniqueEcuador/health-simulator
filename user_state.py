# Health Simulator V1 — CoreFlow
# user_state.py
#
# Dit is de centrale plek waar alles over de gebruiker wordt bijgehouden.
# Door alles hier samen te zetten, hoeven we later nooit door de hele
# code te zoeken als we iets willen toevoegen of aanpassen.

user_state = {

    # --- ENERGIE & VERMOEIDHEID ---
    "energie_niveau": 70,        # 0-100: hoe energiek voelt de gebruiker zich nu?
    "vermoeidheid": 30,          # 0-100: hoe moe? (niet altijd het omgekeerde van energie)

    # --- SLAAP ---
    "slaap_uren": 7.0,           # hoeveel uur geslapen afgelopen nacht

    # --- ACTIVITEIT ---
    "activiteit_vandaag": "licht",  # "rust", "licht", "matig", "intensief"

    # --- OMGEVING ---
    "temperatuur_gevoeligheid": False,  # True als gebruiker temperatuurgevoelig is (bijv. MS)

    # --- UITBREIDBAAR LATER ---
    # "spoons_beschikbaar": 10,   # voor spoon theory model (V2)
    # "crash_risico": 0.0,        # 0.0-1.0, berekend door simulator (V2)
    # "stress_niveau": "laag",    # (V2)
}
