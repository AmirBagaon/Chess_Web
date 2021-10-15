from django.shortcuts import render

from django.http import HttpResponse
import json
from django.shortcuts import *
from django.template import RequestContext
import json
from django.shortcuts import *
from django.template import RequestContext

# Create your views here.

def chess_view(request):
    return render(request, "main/chess.html")