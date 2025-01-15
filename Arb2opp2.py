# Opp2) Jeg har brukt gammel forelesninger for å løse denne oppgave#
#Brukt google og AI for å finne hvilken funksjon passer best for å komme til nærmeste hele tal#
#Importert math for å kunne bruke math.ceil#

import math

Antall_elever = int(input("Hvor mange elever skal spise pizza? "))

Antall_pizzaer = math.ceil(Antall_elever / 4)

print ("Det skal handles", Antall_pizzaer," pizzaer til festen.")