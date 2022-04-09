from django.shortcuts import render
#import pizza form dari forms.py
from .forms import PizzaForm

def home(request):
    return render(request, 'pizza/home.html') 

def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thans for Ordering, dengan ukuran %s, %s, %s' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': new_form, 'note':note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form}) 