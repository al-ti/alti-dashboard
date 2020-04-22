from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.ventusdashboard import dashboard


class ventus_panel(horizon.Panel):
    name = _("ventus_panel")
    slug = "ventus_panel"


dashboard.ventusdashboard.register(ventus_panel)
