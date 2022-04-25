from django.shortcuts import render
import requests, locale
import pandas as pd
from bs4 import BeautifulSoup
from .forms import SearchForm
from django.http import HttpResponseRedirect
from PIL import Image
from io import BytesIO

def ip(request):
    response = requests.get('http://demo.ip-api.com/json')
    geodata = response.json()
    return render(request, 'cek_loc/home.html', {
        'citi': geodata['city'],
        }
    )

def ip2(request):
    response = requests.get('http://demo.ip-api.com/json')
    geodata = response.json()
    return render(request, 'cek_loc/home.html', {
        'citi': geodata['city'],
        }
    )

def scrap(request):
    if request.method == 'POST':
        filled_form = SearchForm(request.POST)
        baseurl = "https://www.google.com/search?q=beli+"+filled_form+"&sxsrf=APq-WBt4jLZxrfwaRP4YeYUhlfB-EWkTlw:1649653964236&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjEnan0n4v3AhUNRmwGHTIVDlQQ_AUoAnoECAEQBA&biw=1365&bih=937&dpr=1"
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
        r = requests.get(url=baseurl, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        productlist = soup.find_all('div', class_='VOo31e')
        productlinks = []
        for item in productlist:
            for link in item.find_all('a', href=True):
                productlinks.append("https://google.com"+link['href'])
        return render(request, 'cek_loc/home.html', {
            'productlinks': productlinks,
            }
        )


def orders(request):

    if request.method == 'POST':
        filled_form = SearchForm(request.POST)
        if filled_form.is_valid():
            baseurl = "https://www.google.com/search?q=%s&sxsrf=APq-WBuyx07rsOeGlVQpTsxLt262WbhlfA:1650636332756&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjQr5HC66f3AhXxxzgGHejKC9sQ_AUoAXoECAIQAw&biw=1920&bih=937&dpr=1"%(filled_form.cleaned_data['s'])
            headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
            r = requests.get(url=baseurl, headers=headers)
            r_images = requests.get(url=baseurl)
            
            soup = BeautifulSoup(r.content, 'lxml')

            soup_for_image = BeautifulSoup(r_images.text, 'html.parser') 
            productlist = soup.find_all('div', class_='VOo31e')
            # print(productlist)
            productlinks = []

            #find product links
            for item in productlist:
                for link in item.find_all('a', href=True):
                    # print(link['href'])
                    productlinks.append("https://google.com"+link['href'])

            #find product images
            productimages = [] 
            product_images = soup_for_image.findAll('img')
            for item in product_images:
                # print(item['src'])
                if "data:image/svg+xml" not in item['src']:
                    productimages.append(item.get('src'))

            #find product price
            productprices = []
            product_prices = soup.find_all('span', class_='a8Pemb OFFNJ')
            for prices in product_prices:
                # print(prices)
                productprices.append(prices.text)

            #find product name
            productnames = []
            product_names = soup.find_all('h4', class_='Xjkr3b')
            for names in product_names:
                print(names.text)
                productnames.append(names.text)

            #sorting data
            new_prices = list(map(lambda price: int(price.replace('.', '').replace(',00', '').strip('Rp. ')), productprices))
            final_list = list(zip(productlinks, productnames, new_prices, productimages))
            sorted_list = pd.DataFrame(final_list).sort_values(by = 2).values

            return render(request, 'cek_loc/home.html', {
                'data': sorted_list
                }
            )
    else:
        return render(request, 'cek_loc/home.html')
