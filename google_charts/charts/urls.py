from django.contrib import admin
from django.urls import path
from charts import views
from .views import *


urlpatterns = [
	path('',views.home, name='home'),
    path('circle_add/', views.circle_add, name='circle_add'),
]
