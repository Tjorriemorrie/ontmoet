from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


def question(request):
    return HttpResponse("Question page")
