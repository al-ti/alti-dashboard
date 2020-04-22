from horizon import tabs

from openstack_dashboard.dashboards.ventusdashboard.ventus_panel \
    import tabs as ventusdashboard


class IndexView(tabs.TabbedTableView):
    tab_group_class = ventusdashboard.MypanelTabs
    template_name = 'ventusdashboard/ventus_panel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
