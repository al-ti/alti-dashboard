from django.utils.translation import ugettext_lazy as _

import horizon


class VentusDashboard(horizon.Dashboard):
   name = _("Ventus")
   slug = "ventusdashboard"
   panels = ('ventusservers',)           # Add your panels here.
   default_panel = 'ventusservers'    # Specify the slug of the dashboard's default panel.

class VentusCompute(horizon.PanelGroup):
    slug = "ventuscompute"
    name = _("Ventus compute")
    panels = ('ventusservers',)

horizon.register(VentusDashboard)
