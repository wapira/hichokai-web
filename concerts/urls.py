from django.urls import path
from . import views

urlpatterns = [
    path('', views.concert_list, name='concert_list'),
    path('<int:pk>/', views.concert_detail, name='concert_detail')
]
