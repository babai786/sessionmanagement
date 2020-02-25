from django.shortcuts import render
from . import forms


def additem(request):
    form=forms.Additemform()
    if request.method=="POST":
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'pratikapp/additem.html',{'form':form})

def  display(request):
    return render(request,'pratikapp/display.html')
