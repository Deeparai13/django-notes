from django.shortcuts import render
from djangoapp.models import Posts

# Create your views here.
def post(request):
    conten=Posts.objects.all()
    
    collect={
        "type":conten
    }
    
    return render(request,'djangoapp/index.html',collect)

def detail(request,pk):
    match=Posts.objects.get(pk=pk)
    game={
        "top":match
    }
    return render(request,"djangoapp/detail.html",game )

def base(request):
    return render(request,"djangoapp/base.html")

def gallery(request):
    return render(request,"djangoapp/gallery.html")

def contact(request):
    return render(request,"djangoapp/contact.html")