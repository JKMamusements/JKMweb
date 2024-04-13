from django.shortcuts import render


from django.http import HttpResponse

def home(request):
    info = {}
    return render(request, "index.html", info)