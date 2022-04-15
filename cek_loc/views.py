from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import SearchForm
from django.http import HttpResponseRedirect

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
            baseurl = "https://www.google.com/search?q=beli+%s&sa=X&biw=1920&bih=880&tbm=shop&sxsrf=APq-WBthh6vre95oa-9ef0cSMsChCA6SAw:1649941428917&tbs=p_ord:p&ei=tBtYYv-gN52h4t4P47yHSA&ved=0ahUKEwj_ypTmzpP3AhWdkNgFHWPeAQkQuw0IkQcoAg"%(filled_form.cleaned_data['s'])
            headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
            r = requests.get(url=baseurl, headers=headers)
            r_images = requests.get(url=baseurl)
            
            soup = BeautifulSoup(r.content, 'lxml')

            # this is for image
            r_images = r_images.text
            #end for image

            soup_for_image = BeautifulSoup(r_images, 'html.parser') 
            productlist = soup.find_all('div', class_='VOo31e')
            productlinks = []

            #find product links
            for item in productlist:
                for link in item.find_all('a', href=True):
                    # print(link['href'])
                    productlinks.append("https://google.com"+link['href'])

            #find product images
            productimages = [] 
            for item in soup_for_image.find_all('img'):
                print(item['src'])
                if "data:image/svg+xml" not in item['src']:
                    productimages.append(item.get('src'))

            #find product price
            productprices = []
            product_prices = soup.find_all('span', class_='a8Pemb OFFNJ')
            for prices in product_prices:
                productprices.append(prices.text)

            #find product name
            productnames = []
            product_names = soup.find_all('h4', class_='Xjkr3b')
            for names in product_names:
                productnames.append(names.text)

            return render(request, 'cek_loc/home.html', {
                'data': zip(productlinks,productprices, productimages, productnames)
                }
            )
    else:
        return render(request, 'cek_loc/home.html')
