from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from random import choice

from .models import Problem

def index(request):
    template = loader.get_template("problems/index.html")
    context = {"problem": choice(list(Problem.objects.all()))}
    return HttpResponse(template.render(context, request))

def correct(request):
    template = loader.get_template("problems/correct.html")
    return HttpResponse(template.render({}, request))

def incorrect(request):
    template = loader.get_template("problems/incorrect.html")
    return HttpResponse(template.render({}, request))

def answer(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    try:
        answer = int(request.POST["answer"])
    except KeyError:
        # Redisplay the problem.
        return render(
            request,
            "problems/index.html",
            {
                "problem": problem,
                "error_message": "You didn't enter an answer.",
            },
        )
    else:
        if problem.check_answer(answer):
            return HttpResponseRedirect(reverse("problems:correct"))
        else:
            return HttpResponseRedirect(reverse("problems:incorrect"))