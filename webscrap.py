import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}

class Webscrap:
    def __init__(self):
        self.WEBSITE = "https://www.amazon.ca/Google-Pixel-Watch-Silver-White/dp/B0CCQ4BX4T/?_encoding=UTF8&pd_rd_w=5USzt&content-id=amzn1.sym.19590cf9-c3a1-4f11-8955-56f5584e58c3&pf_rd_p=19590cf9-c3a1-4f11-8955-56f5584e58c3&pf_rd_r=5A71VX4K6STA0F4BJTSH&pd_rd_wg=G1jnb&pd_rd_r=adcfb08d-ab15-45d5-ade4-4c3400caabe2&ref_=pd_hp_d_atf_dealz_cs&th=1"
        self.get_price()
    def get_price(self):
        responce = requests.get(url=self.WEBSITE, headers=headers)
        contents = responce.text
        soup = BeautifulSoup(contents, "html.parser")
        price = soup.find(name="span", class_="a-offscreen").getText()
        # print(price)
        price = price.replace("$", "")
        # print(price)
        return price


w = Webscrap()




