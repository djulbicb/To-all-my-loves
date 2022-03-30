import requests
from bs4 import BeautifulSoup
import re
import smtplib
import os
import time
import datetime
from Product import Product
# http://myhttpheader.com/
URL:str = "https://www.amazon.com/dp/B00X9JNWGS/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

def stripAlphabetCharacters(string: str):
    return re.sub("[^0-9\.]", "", string)

def getProductFromSoup(soup: BeautifulSoup) :
    title = soup.select_one("#productTitle").text.lstrip().rstrip()
    priceAsStr = soup.select_one(selector="#corePrice_desktop .a-offscreen").text
    price = float(stripAlphabetCharacters(priceAsStr))

    return Product(title=title, price=price)

def readUrlAsBSoup(url:str):
    # headers are required to imitate real user
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept-Language" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }
    response = requests.get(url=URL, headers=headers)
    return BeautifulSoup(response.text, "html.parser")

def sendEmail(product: Product):
    GMAIL_USERNAME = os.environ['GMAIL_USERNAME']
    GMAIL_PASSWORD = os.environ['GMAIL_PASSWORD']

    # za svakog providera drugaciji email server
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.set_debuglevel(0)
        connection.starttls()  # da se pokrene tls security
        connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)
        # subject:Za naslov

        connection.sendmail(from_addr=GMAIL_USERNAME,
                            to_addrs=GMAIL_USERNAME,
                            msg="Subject:Hello\n\nHello Hello" + product.to_email())
        connection.close()

# MAIN
##############################################################
lastPrice:float = None
while True:
    soup = readUrlAsBSoup(url=URL)
    product = getProductFromSoup(soup)

    if (lastPrice is None):
        lastPrice = product.price

    if lastPrice == product.price:
        print("Sending invite")
        sendEmail(product)
    else:
        print("Different price")

    print(product)
    time.sleep(1)


