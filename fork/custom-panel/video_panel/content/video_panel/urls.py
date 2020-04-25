from django.conf.urls import url

from video_panel.content.video_panel import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
