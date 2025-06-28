from webscrap import Webscrap
from smtp import Send_email

webscrape = Webscrap()
current_price = float(webscrape.get_price())
print(current_price)

email = Send_email()

if current_price <= 270:
    email.send_mail("price alert", "There is a deal on the watch you want, go get it boy", webscrape.WEBSITE)
else:
    print("no deals right now")