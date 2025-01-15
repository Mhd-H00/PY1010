# Opp 5 gamle forelesning brukt, google, mimo appen og ai. Det er mulig å forbedre.
# koden med Float og input for å kunne leke lett å endre på tallene.

import math

def beregn_figur_egenskaper(a, b):
    # Arealberegninger
    radius = a
    halvsirkel_areal = (1 / 2) * math.pi * radius**2
    trekant_areal = (1 / 2) * a * b
    total_areal = halvsirkel_areal + trekant_areal

    # Beregninger av ytre omkrets
    halvsirkel_omkrets = math.pi * radius  # Halvparten av omkretsen til en sirkel
    hypotenus = math.sqrt(a**2 + b**2)
    ytre_omkrets = halvsirkel_omkrets + b + hypotenus

    # resultat
    return total_areal, ytre_omkrets

   # Eksempel
a = 5  # erstatt med ønsket verdi for 'a'
b = 10  # erstatt med ønsket verdi for 'b'
areal, omkrets = beregn_figur_egenskaper(a, b)
   
print(f"Totalt areal: {areal:.2f}")
print(f"Ytre omkrets: {omkrets:.2f}")