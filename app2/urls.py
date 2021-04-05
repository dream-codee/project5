from django.urls import path
from app2 import views
app_name="app2"

urlpatterns=[
    path('index/',views.index,name="index"),
    path("sample2/",views.sample2,name="sample2"),
]