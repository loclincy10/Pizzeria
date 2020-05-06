from django.urls import path

from . import views 


app_name = 'pizzas'


urlpatterns = [
    # second arg is func to call in views.py
    # third arg is name for URL pattern to refer to it later
    path('',views.index, name='index'), #refers to index func in views
    path('pizzas',views.pizzas, name='pizzas'),
    # the int value is stored in the variable pizza_id and will
    # be then passed to the pizza function in views.py
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'), #pathway is dynamic
    path('new_comment/<int:pizza_id>/',views.new_comment, name='new_comment'),
]

#creates path for each indiv webpage^^^^