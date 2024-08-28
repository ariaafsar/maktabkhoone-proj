from django.urls import path
from teacher_app.views import  teacher_list

urlpatterns = [path("", teacher_list)]
