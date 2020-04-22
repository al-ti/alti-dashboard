from horizon import views


class IndexView(tabs.TabbedTableView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    # A very simple class-based view...
    template_name = 'ventus_dashboard/ventus_panel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
