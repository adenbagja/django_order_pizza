from django.shortcuts import render
import requests

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