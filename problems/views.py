from django.http import HttpResponse
from django.template import loader
from random import choice

from .models import Problem

def index(request):
    template = loader.get_template("problems/index.html")
    context = {"problem": choice(list(Problem.objects.all()))}
    return HttpResponse(template.render(context, request))