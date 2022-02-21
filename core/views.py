from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos </h1>'.format(nome,idade))
    # return HttpResponse('<h1>Hello World...</h1>')

def soma(request, n1,n2,n3):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(n1,n2,n1+n2))

def divide(request, n1,n2,n3):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(n1,n2,n1/n2))

def sub(request, n1,n2,n3):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(n1,n2,n1-n2))