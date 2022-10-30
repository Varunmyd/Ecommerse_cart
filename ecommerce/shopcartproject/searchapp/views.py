from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from shopapp.models import product
from shopapp.views import allprodcat


# Create your views here.



def searchresult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query))
        return render(request,'search.html',{'query':query,'products':products})

