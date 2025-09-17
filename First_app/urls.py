from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Keyur", views.Keyur, name="Keyur"),
    path("<str:name>", views.Greet, name="Greet")
]
