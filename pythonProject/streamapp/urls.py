from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('facecam_feed', views.facecam_feed, name='facecam_feed'),
]
