from django.urls import path
from . import views

urlpatterns=[
    path('',views.states),
    path('about/',views.about)
]