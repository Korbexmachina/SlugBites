"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import foodItem
from . import get_data

food_data = get_data()

# Create your views here.


def index(response) -> HttpResponse:
    return HttpResponseRedirect("/home")


def home(response) -> HttpResponse:
    curr = food_data.get_day().get_category("Entrees")
    c9 = curr.get_location('College Nine/John R Lewis')
    cow = curr.get_location("Cowell/Stevenson")
    cro = curr.get_location("Crown/Merrill")
    por = curr.get_location("Porter/Kresge")
    return render(response, "main/home.html", {"C9": c9, "COW": cow, "CRO": cro, "POR": por})


def food(response) -> HttpResponse:
    # Displays all possible menu items
    return render(response, "main/food.html", {"food": food_data.full_menu()})


def currentmeal(response) -> HttpResponse:
    return HttpResponseRedirect("/home")


def search(response) -> HttpResponse:
    print(response.GET)
    results = food_data.search(response.GET['search'])
    print(results)
    return render(response, "main/searchresults.html", {"meals": results})
    pass
