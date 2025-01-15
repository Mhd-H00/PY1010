# Har installert conutryinfo bibliotek. I kernel pip install countryinfo.
from countryinfo import CountryInfo


name=input("Enter your country : ")


country = CountryInfo(name)


print("Capital is : ",country.capital())


print("Currencies is :",country.currencies())


print("Language is : ",country. languages())


print("Borders are : ",country.borders())


print("Provinces are : ", country.provinces())


print("Area are : ", country.area())


print("Calling are : ", country.calling_codes())


print("Capital Latitudes and Longitudes are : ", 
                          country.capital_latlng())


print("TimeZone : ", country.timezones())


print("Population : ", country.population())


print("Others names : ",country.alt_spellings())

