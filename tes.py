import requests, base64
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

baseurl = "https://www.google.com/search?q=beli+anjing&sxsrf=APq-WBt4jLZxrfwaRP4YeYUhlfB-EWkTlw:1649653964236&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjEnan0n4v3AhUNRmwGHTIVDlQQ_AUoAnoECAEQBA&biw=1365&bih=937&dpr=1"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
r = requests.get(url=baseurl, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all('div', class_='VOo31e')
product_images = soup.find_all('div', class_='ArOc1c')

# product_images = soup.find_all('div', class_='XrAfOe')

# product_names = soup.find_all('h4', class_='Xjkr3b')
# for names in product_names:
#     print(names.text)

# for prices in product_images:
#     for price in prices.find_all('span', class_='a8Pemb OFFNJ'):
#         print(price.text)


for item in product_images:
    for image in item.find_all('img', src=True):
        print(Image.open(BytesIO(base64.b64decode(str(image['src'])))))
        

# print(productlist)
# productlinks = []
# for item in productlist:
#     for link in item.find_all('a', href=True):
#                 print("https://google.com"+link['href'])

# product_images_list = []
# for item in product_images:
#     for image in item.find_all('img', src=True):
#                 print(image['src'])


# import requests 
# from bs4 import BeautifulSoup 
    
# def getdata(url): 
#     headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
#     r = requests.get(url, headers=headers) 
#     return r.text 
    
# htmldata = getdata("https://www.tokopedia.com/search?st=product&q=kucing&srp_component_id=02.01.00.00&navsource=home") 
# soup = BeautifulSoup(htmldata, 'html.parser') 
# productimages = soup.find_all('div', class_='responsive css-1eg7f6s')
# # print(productimages)
# for item in productimages:
#     print(item)
#     for item2 in item.find('img'):
    #     print(item2['src'])
#         print(item2.get('src'))

# from re import sub
# from decimal import Decimal

# money = '$6,150,593.22'
# value = Decimal(sub(r'[^\d.]', '', money))
# print(value)