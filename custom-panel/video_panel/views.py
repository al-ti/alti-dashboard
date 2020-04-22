from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'identity/video_panel/index.html'
