#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import uuid


def index(request):
    return HttpResponse("<pre>Hello, world!\n You have been assign the following uuid: " + str(uuid.uuid4()) + "\n This will be used to identify you for the rest of your life.  Have a nice day.</pre>")