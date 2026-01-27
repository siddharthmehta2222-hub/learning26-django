from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
        return HttpResponse("Hello")
def aboutus(request):
        return render(request,'aboutus.html')
def contactus(request):
        return render(request,'contactus.html')