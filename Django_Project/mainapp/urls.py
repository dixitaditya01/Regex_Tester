from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('check_regex/',views.check_regex)
]