from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Reviews


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj2 = Reviews.objects.all()
    return render(request, "index.html", {'result': obj, 'vie': obj2})

#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request, "result.html",{'result':res})
# def contact(request):
#     return HttpResponse("contact details")
