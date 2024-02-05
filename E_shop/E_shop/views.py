from django.shortcuts import render
from shop.models import category,subcategory

def master(request):
    return render(request,'master.html')

def index(request):
    cat=category.objects.all()
    context={
        "cat":cat,
    }
    return render(request,'index.html',context)