from django.shortcuts import render

from django.http import HttpResponse
import json
from django.shortcuts import *
from django.template import RequestContext, context
import json
from django.shortcuts import *
from django.template import RequestContext

from main.dataHandler import DataHanlder

# Create your views here.

def chess_view(request):
    return render(request, "main/chess.html")

def welcome(request):
    return render(request, "main/welcome.html")

def randomPlay(request):
    data = DataHanlder.getRandomPlay()
    context = {'data' : data}
    return render(request, "main/chess.html", context)

def onevsone(request):
    data = DataHanlder.getOneVsOne()
    context = {'data' : data}
    return render(request, "main/chess.html", context)

def vsAI(request):
    data = DataHanlder.getVsAI()
    context = {'data' : data}
    return render(request, "main/chess.html", context)

def temp(request):
    print("$$$$$$$$$$$$$$ HERE")
    returnValue = ""
    data = ""
    if request.method == "POST":
        print(request.POST)
        data = request.POST["input_area"]

        
    if request.method == "GET":
        print("$$$$$$$$$$$$$$ In GET")
        data = request.GET.get('f', '')
        print(data)

    handler = DataHanlder(data)
    returnDictValues = handler.handle()
        
    return HttpResponse(json.dumps(returnDictValues), content_type="application/json")

    # returnValue = handler.handle()
        
    # return HttpResponse(json.dumps({'message': returnValue}), content_type="application/json")
