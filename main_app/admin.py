from django.contrib import admin
from .models import Finch, Feeding, Toy

if not admin.site.is_registered(Finch):
    admin.site.register(Finch)

if not admin.site.is_registered(Feeding):
    admin.site.register(Feeding)

if not admin.site.is_registered(Toy):
    admin.site.register(Toy)