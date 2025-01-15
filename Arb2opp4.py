# Opp4) Jeg har brukt forelesninger, Mimo appen (mobil telefon app, som jeg bruke for å trene) python og ai modul, AI. Her vurdert
#å bruke tuppel, jeg kunne ikke det, til slutt fant jeg at tuppel passer best for
#fast informasjon som kan ikke endres for eksempel fødselsdato, navn etternavn.


# Dictionary som array
country_data = {
    "England": {"capital": "London", "population": 8.982},
    "Norway": {"capital": "Oslo", "population": 0.537},
    "Sweden": {"capital": "Stockholm", "population": 1.03},
    "Denmark": {"capital": "Copenhagen", "population": 0.583}
}

# Funksjon for å skrive ut informasjon om landet
def print_country_info(country):
    data = country_data.get(country)
    if data:
        print(f"{data['capital']} er hovedstaden i {country} og det er {data['population']} mill. innbyggere i {data['capital']}.")
    else:
        print(f"{country} finnes ikke i dictionaryen.")

# Funksjon for oppdatere informoasjon om landet.
def update_country_data(country, capital, population):
    country_data[country] = {"capital": capital, "population": population}
    print(f"Informasjonen om {country} er oppdatert/lagt til.")

# Hovdprogram
while True:
    action = input("Vil du søke etter et land eller legge til et nytt? (søk/legg til/avslutt): ").lower()
    if action == 'søk':
        country = input("Skriv inn et land: ")
        print_country_info(country)
    elif action == 'legg til':
        country = input("Skriv inn navnet på landet: ")
        capital = input("Skriv inn hovedstaden: ")
        population = float(input("Skriv inn antall innbyggere (i millioner): "))
        update_country_data(country, capital, population)
    elif action == 'avslutt':
        break
    else:
        print("Ugyldig valg. Vennligst prøv igjen.")

# Å printe ut oppdatert dictionaryen
print("Oppdatert dictionary:")
for country, info in country_data.items():
    print(f"{country}: Hovedstad - {info['capital']}, Innbyggere - {info['population']} mill.")
