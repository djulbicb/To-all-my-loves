from bs4 import BeautifulSoup

with open("website.html") as file:
    contets = file.read()
    
soup = BeautifulSoup(contets, "html.parser") # mora da mu se naglasi parser
h1 = soup.select_one("h1")
print(h1.text)
