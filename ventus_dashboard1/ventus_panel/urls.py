from django.conf.urls import url

from openstack_dashboard.dashboards.ventusdashboard.ventusservers import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
