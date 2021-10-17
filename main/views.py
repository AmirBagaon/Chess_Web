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
    if request.method == "POST":
        print(request.POST)
        data = request.POST["input_area"]

        handler = DataHanlder(data)
        returnValue = handler.handle()
        
    return HttpResponse(json.dumps({'message': returnValue}), content_type="application/json")
