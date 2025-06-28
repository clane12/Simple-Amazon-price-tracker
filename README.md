🔔 Amazon Price Alert
A Python script that monitors the price of a product on Amazon and sends you an email notification when the price drops below a target threshold. Uses web scraping and SMTP email integration to automate alerts.

✨ Features
🕸️ Scrapes product price directly from Amazon.

🎯 Alerts only when the price falls below a set threshold.

📧 Sends a custom email with product details and direct link.

🔐 Uses environment variables to protect sensitive credentials.

📦 Requirements
Python 3.x+

A Gmail account with “Less Secure Apps” or App Password enabled.

A .env file with your credentials:

EMAIL=your_email@gmail.com
PASSWORD=your_password_or_app_password

Required Libraries:

pip install requests beautifulsoup4 python-dotenv
🚀 How to Run
Clone or download the repository.

Create a .env file in the same directory:

EMAIL=your_email@gmail.com
PASSWORD=your_email_password
Open main.py (or the script that runs Webscrap and Send_email) and update:

The product URL in the Webscrap class.

Your target price in the if current_price <= ... line.

The recipient's email in the send_mail() method (if needed).

Run the script:

python main.py
🎮 How It Works
✅ Webscrap.py: Scrapes the Amazon product page to extract the current price using BeautifulSoup.

📧 smtp.py: Sends an email if the price drops below the defined threshold.

🧠 main.py: Ties everything together—fetches price, checks threshold, and sends email alerts.

📧 Email Example
Subject: price alert

Body:

There is a deal on the watch you want, go get it boy
https://www.amazon.ca/Google-Pixel-Watch-Silver-White/dp/...
🧩 Future Enhancements
📆 Schedule the script to run daily using cron (Linux/macOS) or Task Scheduler (Windows).

📱 Send SMS using Twilio API.

💵 Support multiple products and dynamic thresholding.

📊 Log price history in CSV or database.

⚠️ Disclaimer
Amazon may block automated requests. Use with caution and respect the website's terms of service.
