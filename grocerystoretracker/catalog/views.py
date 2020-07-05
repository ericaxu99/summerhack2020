from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import (Item, Consumer, Store)
# Create your views here.


def home(request):
    num_items = Item.objects.all().count()
    budget_left = Consumer.budget  # sum of price of all items

    context = {
        'num_items': num_items,
        'budget_left': budget_left,
    }

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'home.html', context=context)
