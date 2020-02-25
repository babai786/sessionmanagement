from django.shortcuts import render
from . import forms

# Create your views here.
def name_view(request):
    form=forms.Nameform()
    return render(request,'pratikapp/name.html',{'form':form})



def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=forms.Ageform()
    return render(request,'pratikapp/age.html',{'form':form})

def gfname_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=forms.Gfform()
    return render(request,'pratikapp/gfname.html',{'form':form})

def result(request):
    gfname=request.GET['gfname']
    request.session['gfname']=gfname
    return render(request,'pratikapp/result.html')
