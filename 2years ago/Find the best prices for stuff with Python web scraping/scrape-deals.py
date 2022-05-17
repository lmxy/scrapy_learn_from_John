import requests
from bs4 import BeautifulSoup
import smtplib

url_cpu = 'https://www.scan.co.uk/products/amd-ryzen-5-3600-am4-zen-2-6-core-12-thread-36ghz-42ghz-turbo-32mb-l3-pcie-40-65w-oem'
url_motherboard = 'https://www.scan.co.uk/products/open-box-msi-b450m-mortar-max-amd-b450-s-am4-ddr4-sata3-2xm2-2-way-crossfire-realtek-gbe-usb-32-gen2'
url_ram = 'https://www.scan.co.uk/products/16gb-2x8gb-corsair-ddr4-vengeance-lpx-black-pc4-25600-3200-non-ecc-unbuff-cas-16-135v-amd-ryzen-opti'

def get_price(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span', attrs={'itemprop': "price"})['content']
    return price

def add_price(p1, p2, p3):
    total = (float(p1) + float(p2) + float(p3))
    return total

def send_email():
    server = smtplib.SMTP('smtp.163.com', 25)
    server.starttls()
    server.login("wjzxyaowei@163.com", "KXFBZJUTUKUIYAJS")
    subject = 'Important email information'
    body = f'INFO:{total_price}'
    message = f'Subject:{subject}\n\n{body}'
    server.sendmail('wjzxyaowei@163.com', '280048796@qq.com', message)
    print('Email sent')
    server.quit()

# cpu = get_price(url_cpu)
# motherboard = get_price(url_motherboard)
# ram = get_price(url_ram)

# total_price = add_price(cpu, motherboard, ram)
total_price = "KXFBZJUTUKUIYAJS"
send_email()



