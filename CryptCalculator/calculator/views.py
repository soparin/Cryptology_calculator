from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 align=center>Welcome to the <b>cryptology calculator</b></h1>")

def euclidIndex(requst):
    return HttpResponse("<h1 align=center>Euclid algorithm.</h1>")

def sundaramIndex(request):
    return HttpResponse("<h1 align=center>Sundaram algorithm to find some simple numbers.</h1>")

def algorithm(request, algo):
    return HttpResponse(f"<h1 align=center> {algo}</h1>")
