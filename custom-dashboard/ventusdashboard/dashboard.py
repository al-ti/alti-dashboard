from django.utils.translation import ugettext_lazy as _

import horizon


class ventusdashboard(horizon.Dashboard):
   name = _("ventusdashboard")
   slug = "ventusdashboard"
   panels = ('ventus_panel',)           # Add your panels here.
   default_panel = 'ventus_panel'    # Specify the slug of the dashboard's default panel.

class ventuscompute(horizon.PanelGroup):
    slug = "ventuscompute"
    name = _("Ventus compute")
    panels = ('ventus_panel',)

horizon.register(ventusdashboard)
