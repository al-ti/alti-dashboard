from django.utils.translation import ugettext_lazy as _
import horizon


class video_panel(horizon.Panel):
    name = _("My Panel")
    slug = "video_panel"
