from django.shortcuts import render

def count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    return render(request,'pratikapp/count.html',{'count':newcount})
    
