from django.contrib import admin

# Register your models here....with the Admin site
from .models import Pizza

admin.site.register(Pizza)