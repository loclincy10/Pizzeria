from django.contrib import admin

# Register your models here....with the Admin site
from .models import Pizza, Topping#, Comment

admin.site.register(Pizza)

admin.site.register(Topping)

#admin.site.register(Comment)