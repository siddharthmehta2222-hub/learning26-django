from django.contrib import admin
from django.urls import path
from . import views   

urlpatterns = [
    path('', views.contactus),
    path('', views.aboutus),
    path('', views.test),
    path('admin/', admin.site.urls),
    path('test/', views.test),   
    path("about/",views.aboutus),
    path("contact/",views.contactus),
    path("recap/",views.recap),
    path("recipe/",views.recipe),
    path("iplteams/",views.iplteams),
]
