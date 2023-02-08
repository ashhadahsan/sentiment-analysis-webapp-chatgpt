from .views import YoutubeView
from django.urls import path

urlpatterns = [path("youtube/", YoutubeView.as_view())]
