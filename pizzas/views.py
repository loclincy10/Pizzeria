from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Pizza#, #Topping

# Create your views here.

def index(request):
    # the home pg
    return render(request, 'pizzas/index.html') #return request along with the pg

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context) #context contain dict of info needed for webpg, makes it dynamic
    # pizzas/pizzas is the folder for html

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id) 

    toppings = pizza.topping_set.all()#order_by('-date_added') # we can access toppings bc hay PK/FK relation
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)

            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    
    context = {'form': form, 'pizza': pizza}
    return render(request, 'pizzas/new_comment.html', context)
                                            
