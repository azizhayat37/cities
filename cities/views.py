from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import City

# Create your views here.
def city_list(request):
    cities = City.cities()
    paginator = Paginator(cities, 50) #show 50 cities per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '/Users/azizhayat/Documents/cities/cities/templates/cities/city_list.html', {'page_obj': page_obj})

def city__by_name(request, city):
    cities = City.city_by_name(city)
    paginator = Paginator(cities, 50) #show 50 cities per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '/Users/azizhayat/Documents/cities/cities/templates/cities/city_list.html', {'page_obj': page_obj})