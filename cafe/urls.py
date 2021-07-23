from django.urls import path

from . import views

urlpatterns = [
    path("", views.CafeView.as_view())
]
