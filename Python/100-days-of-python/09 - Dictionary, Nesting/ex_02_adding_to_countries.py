countries = [
  {
    "country" : "France",
    "visits" : 12,
    "cities" : ["Paris", "Lille", "Dijon"]
  },
  {
    "country" : "Germany",
    "visits" : 5,
    "cities" : ["Berling", "Hamburg", "Stuttgart"]
  }
]

def addToCountries(countryName, numOfVisits=0, cities=[]) :
  newCountry = {
    "country" : countryName,
    "visits" : numOfVisits,
    "cities" : cities
  }

  countries.append(newCountry)

# MAIN
# -----------------------------------------------------------
addToCountries ("Netherland", 10, ["Amsterdam", "Rotterdam"])
print(countries)