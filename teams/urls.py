from django.urls import path
from .views import KopaView, KopaDetailView

urlpatterns = [
    path("teams/", KopaView.as_view()),
    path("teams/<int:team_id>/", KopaDetailView.as_view()),
]
