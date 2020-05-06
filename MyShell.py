import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()
#####################################
from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

p = Pizza.objects.get(id=1)
print(p.name)
print(p.date_added)

#to get data thru a fk relationship, you use the lowercase name of the
# related model followed by an underscore and the word set
toppings = p.topping_set.all()

for topping in toppings:
    print(topping)