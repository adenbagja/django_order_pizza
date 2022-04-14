# import requests
# from bs4 import BeautifulSoup

# baseurl = "https://www.google.com/search?q=beli+anjing&sxsrf=APq-WBt4jLZxrfwaRP4YeYUhlfB-EWkTlw:1649653964236&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjEnan0n4v3AhUNRmwGHTIVDlQQ_AUoAnoECAEQBA&biw=1365&bih=937&dpr=1"
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
# r = requests.get(url=baseurl, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')
# productlist = soup.find_all('div', class_='VOo31e')
# product_images = soup.find_all('div', class_='ArOc1c')

# product_images = soup.find_all('div', class_='XrAfOe')

# product_names = soup.find_all('h4', class_='Xjkr3b')
# for names in product_names:
#     print(names.text)

# for prices in product_images:
#     for price in prices.find_all('span', class_='a8Pemb OFFNJ'):
#         print(price.text)


# for item in product_images:
#     for image in item.find_all('img', src=True):
#         print(image)

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
#     r = requests.get(url) 
#     return r.text 
    
# htmldata = getdata("https://www.google.com/search?q=beli+anjing&sxsrf=APq-WBt4jLZxrfwaRP4YeYUhlfB-EWkTlw:1649653964236&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjEnan0n4v3AhUNRmwGHTIVDlQQ_AUoAnoECAEQBA&biw=1365&bih=937&dpr=1") 
# soup = BeautifulSoup(htmldata, 'html.parser') 
# for item in soup.find_all('img'):
#     print(item['src'])

from re import sub
from decimal import Decimal

money = '$6,150,593.22'
value = Decimal(sub(r'[^\d.]', '', money))
print(value)