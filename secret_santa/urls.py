from django.urls import path

from . import views

urlpatterns=[
    path('', views.Page.as_view(), name='index')

]