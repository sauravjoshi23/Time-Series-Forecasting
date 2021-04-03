from django.shortcuts import render
from json import dumps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import *
from .futureweeksprediction import *
from .pastweeksprediction import *

# Create your views here.
def index(request):

    data = Item.objects.all()

    model_data = []
    for dict in data:
        val1 = dict.Date
        val2 = dict.Sales
        model_data.append({'Date': val1, 'Sales': val2})

    return render(request, 'index.html', {'model_data': model_data})

# Endpoint 1 for future weeks form
def futureweeks(request):
    if request.method == 'POST':
        weeks = request.POST.get('weeks', None)
        ci = request.POST.get('ci', None)
        if weeks and int(ci) != 100:
            futureweekslist = futureweeksprediction(int(weeks), int(ci))
            print(futureweekslist)
            responsejson = json.dumps(futureweekslist)
            print('Below: ', responsejson)
            return JsonResponse(responsejson, safe=False)

# Endpoint 2 for past recent weeks form
def pastweeks(request):
    if request.method == 'POST':
        weeks = request.POST.get('weeks', None)
        ci = request.POST.get('ci', None)
        if weeks and int(ci) != 100:
            pastweekslist = pastweeksprediction(int(weeks), int(ci))
            print(pastweekslist)
            responsejson = json.dumps(pastweekslist)
            print('Below: ', responsejson)
            return JsonResponse(responsejson, safe=False)