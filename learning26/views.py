from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
        return HttpResponse("Hello")
def aboutus(request):
        return render(request,'aboutus.html')
def contactus(request):
        return render(request,'contactus.html')
def home(request):
        return render(request,'homepage.html')
def recap(request):

        return render(request,'recap.html')
def recipe(request):
        ingredients=["maggie","tomato sauce","cheese","onion","spices"]
        data={"name":"maggie","time":2,"ingredients":ingredients}
        return render(request,'recipe.html',data)
def iplteams(request):
        teams=["Chennai Super Kings","Mumbai Indians","Royal Challengers Bangalore","Kolkata Knight Riders","Delhi Capitals","Rajasthan Royals","Punjab Kings","Sunrisers Hyderabad"]
        return render(request,'iplteams.html',{"teams":teams})
