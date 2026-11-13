from django.urls import path
from . import views

app_name = 'concerts'

urlpatterns = [
    path('', views.concert_list, name='list'),
    path('<int:pk>/', views.concert_detail, name='detail')
]
