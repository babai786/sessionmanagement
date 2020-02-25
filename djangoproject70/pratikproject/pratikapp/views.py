from django.shortcuts import render


def cookie_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'pratikapp/wish.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response
