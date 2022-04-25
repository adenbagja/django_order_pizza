import requests, base64
from bs4 import BeautifulSoup


baseurl = "https://www.google.com/search?q=payung&tbs=p_ord:p,vw:g&tbm=shop&sxsrf=APq-WBszHX0yect7l9NP0nOTgujbNmwhWQ:1650624862662&ei=XoliYs27J9eY4-EPw76oyAE&start=0&sa=N&ved=0ahUKEwjN4uHkwKf3AhVXzDgGHUMfChkQ8tMDCMkO&biw=1365&bih=937&dpr=1"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding': 'none',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Connection': 'keep-alive',}
#     'Connection': 'keep-alive',}
r_images = requests.get(url=baseurl)

soup_for_image = BeautifulSoup(r_images.text, 'html.parser') 
# soup_for_image = BeautifulSoup(r_images.content, 'lxml')
# print(soup_for_image)
product_images = soup_for_image.findAll('img')
# print(product_images)
productimages = [] 
for item in product_images:
    print(item['src'])
    
