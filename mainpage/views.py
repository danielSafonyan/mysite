from django.shortcuts import render
from django.http import HttpResponse
AVAILABLE_LINKS = {
    'todos': 'to do app',
    'newyears': 'is it a new year app'
}
# Create your views here.
def index(request):
    return render(request, 'mainpage/index.html', {'links': AVAILABLE_LINKS})