
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('<int:id>', views.home_page, name='home_page'),
    path('update/<int:id>', views.update_clicks, name='update_click'),
    path('', views.start, name='start'),
    path('list', views.select, name='select'),
    path('option', views.click_list, name='click_list'),
]


