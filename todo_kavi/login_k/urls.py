from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
 
    path ("login/",views.login ,name = "login" ),
    # path("taskdetails/",views.taskdetails,name="taskdetails")
    path("taskdetails/<int:id>/<str:title>/",views.taskdetails,name="taskdetails"),
    # path("taskdetail/",views.taskdetails,name="taskdetail")
 
]