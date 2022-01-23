from django.shortcuts import render
from django.views.generic import TemplateView


class DocsView(TemplateView):
    template_name = "index.html"

