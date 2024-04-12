from django.shortcuts import render


from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
# Create your views here.

def home(request):
    info = {}
    return render(request, "home.html", info)