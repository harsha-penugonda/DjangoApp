from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("calc", views.calc, name = "calc"),
    path("notes", views.notes, name = "notes"),
    path("notes/<int:id>", views.deleteNote, name = "notes"),
    path("notes/<int:id>/edit", views.editNote, name = "notes")
]