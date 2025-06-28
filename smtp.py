from smtplib import SMTP
from dotenv import load_dotenv
import os
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")



class Send_email:

    def send_mail(self, subject, message, link):
        mail = SMTP("smtp.gmail.com")
        mail.starttls()
        mail.login(user=EMAIL, password=PASSWORD)
        mail.sendmail(from_addr=EMAIL, to_addrs="yuxithdee@gmail.com", msg=f"subject: {subject}\n\n {message}\n{link}")
        mail.close()

# s = Send_email()
# s.send_mail("h1", "clane", "die")