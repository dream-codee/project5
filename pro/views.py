from django.contrib import admin
from django.urls import path,include
import app1
import app2

urlpatters=[
    path('admin/',admin.site.urls)
    #path('primary_suffix',include("app1.urls"))
    path('',include("app1.urls")),
    path('app2/',include("app2.urls")),
]