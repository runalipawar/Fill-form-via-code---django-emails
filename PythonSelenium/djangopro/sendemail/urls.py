from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-email/', views.send_test_email, name='send-email'),
]

