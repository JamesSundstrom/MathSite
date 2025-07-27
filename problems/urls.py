from django.urls import path

from . import views

app_name = "problems"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:problem_id>/answer", views.answer, name="answer"),
    path("correct", views.correct, name="correct"),
    path("incorrect", views.incorrect, name="incorrect"),
]