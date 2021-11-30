from django.urls import path
from videoapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_gen', views.video_gen, name='video_gen'),
    #3path('webcam_feed', views.webcam_feed, name='webcam_feed'),
 
    ]