from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.ventusdashboard import dashboard


class VentusPanel(horizon.Panel):
    name = _("Ventus Servers")
    slug = "VentusPanel"


dashboard.ventusdashboard.register(VentusPanel)
