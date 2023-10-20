from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('funcky',views.funcky),
    path('danger/<int:guess>', views.danger),
    path('google', views.google),
    path('game/<slug:guess>', views.GameView.as_view())
]