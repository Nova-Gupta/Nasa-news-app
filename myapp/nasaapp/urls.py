from django.urls import path
from . import views  # Ensure that you are importing views from the same directory

urlpatterns = [
    path('', views.index, name='index'),
]
