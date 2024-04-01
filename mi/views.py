from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohith.html')
def sharma(request):
    return HttpResponse('good opener')