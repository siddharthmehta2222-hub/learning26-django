from django.shortcuts import render

# Create your views here.

def studenthome(request):
    return render(request,"studentshome.html")
def studentdashboard(request):
    student ={"name":"John Doe","age":21,"course":"Computer Science","university":"XYZ University"}
    return render(request,"student/studentdashboard.html",{"student":student})