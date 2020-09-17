#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }


def checkPrice(URL):
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    title = soup.find(id = "productTitle").get_text()

    price = soup.find(id = "priceblock_ourprice").get_text()

    converted_price = float(price[1:5])

    #print(title.strip())
    #print(converted_price)

    if converted_price == 450.00:
        
        sendMail()


def sendMail():
    
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.ehlo()

    #tls - Transport Layer security
    server.starttls()
    
    #server.ehlo()

    server.login('nmamatha1808@gmail.com', "PASSWORD")
    
    subject = "Price fell down!!!"
    body = 'Check the amazon link URL = https://www.amazon.in/dp/B07YRSDJY2/ref=cm_sw_r_wa_apa_i_KvkxFbEYG6PVS'
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
            'nmamatha1808@gmail.com',
            '18wh1a1216@bvrithyderabad.edu.in',
            msg)

    print("MAIL SENT")

    server.quit()

URL = "https://www.amazon.in/dp/B07YRSDJY2/ref=cm_sw_r_wa_apa_i_KvkxFbEYG6PVS"

while(True):

    (checkPrice(URL))
    time.sleep(60 ** 3)
