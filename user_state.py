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

# ─────────────────────────────────────────
# 2. JOUW EERSTE FUNCTIE
# ─────────────────────────────────────────

def bereken_energie_advies(state):
    """
    Geeft een eenvoudig advies op basis van de huidige gebruikersstatus.
    'state' is onze user_state dictionary — we geven hem mee aan de functie.
    """

    energie = state["energie_niveau"]
    slaap   = state["slaap_uren"]

    if energie >= 70 and slaap >= 7:
        advies = "Goede dag om actief te zijn. Bewaak je energieniveau elk uur."

    elif energie >= 40 and slaap >= 5:
        advies = "Matige energie. Plan een rustmoment in de middag."

    else:
        advies = "Lage energie of weinig slaap. Prioriteit: herstel boven activiteit."

    return advies
    
# ─────────────────────────────────────────
# TEST DIRECT (optioneel - verwijder later)
# ─────────────────────────────────────────

    if __name__=="__":
        # Test de functie met de huidige staat
        print(=== Health Simulator Test ===")
        print(f"Energie:{user_state['energie_niveau']}")
        print(f"Slaap:{user_state['slaap_uren']}uur")
        print(f"\nAdvies:{bereken_energie_advies(user_state)}")
    
