from django.contrib import admin

#import model pizza and size
from .models import Pizza, Size

# add to dashboard admin
admin.site.register(Pizza)
admin.site.register(Size)
