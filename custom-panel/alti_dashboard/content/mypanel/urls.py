from django.conf.urls import url

from alti_dashboard.content.mypanel import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
