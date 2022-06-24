from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.today()
    is_new_years = now.day == 1 and now.month == 1
    return render(request, 'newyears/index.html', {'is_new_years': is_new_years})
