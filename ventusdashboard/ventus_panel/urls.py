from django.conf.urls import url

from openstack_dashboard.dashboards.ventusdashboard.ventus_panel import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
