from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from scrapper.models import Asset
from .scripts.BankierScrapper import BankierScrapper
from django.db.models.functions import Lower

# Create your views here.

def index(request):
    if request.method == 'GET':
        assets = Asset.objects.all()
        content = {
            'assets': assets
        }
        return render(request, 'scrapper/index.html', content)
    elif request.method == 'POST':
        if request.POST['sort']:
            sort_order = request.POST.get('sort')
            if sort_order == 'asc':
                assets = Asset.objects.all().order_by(Lower('name'))
            elif sort_order == 'desc':
                assets = Asset.objects.all().order_by(Lower('name').desc())
            content = {
                'assets': assets
            }
            return render(request, 'scrapper/index.html', content)
        else:
            return HttpResponseNotFound("Wrong POST data.")