import requests
from bs4 import BeautifulSoup
import smtplib

def checker(URL,threshold_amt):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_saleprice").get_text()[1:].strip().replace(',','')
    Fprice = float(price)
    if Fprice > 3000:
        alert_me(URL,title,price)

def alert_me(URL,title, price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR_GMAIL_ADDRESS','YOUR_GOOGLE_APP_PASSWORD')
    subject = 'Price fell down for '+title
    body = 'Buy it now here: '+URL
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail('sonawaneajinks@gmail.com','sonawaneajinks@gmail.com',msg)
    print('Email alert sent')
    server.quit()


checker('https://www.amazon.in/Nike-Borough-Blk-Plnm-W-Sneakers-6-839977-008/dp/B07DCJ3NGF/ref=sr_1_fkmr0_2?dchild=1&keywords=Nike+boys+court+borough&qid=1578118756&sr=8-2-fkmr0',12345)



