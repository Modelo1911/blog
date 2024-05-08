from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ListPageView(TemplateView):
    template_name = 'pages/list.html'

class NewPageView(TemplateView):
    template_name = 'pages/new.html'
