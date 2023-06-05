from django.urls import path
from .views import KopaView

urlpatterns = [
    path("teams/", KopaView.as_view()),
]
