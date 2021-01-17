import random

from django.http import Http404
from django.shortcuts import render
from .models import Word, Dictionary


def home(request):
    try:
        dic = Dictionary.objects.all()[0]
    except Dictionary.DoesNotExist:
        raise Http404("Dictionary does not exist.")
    try:
        # yield some 6 words
        l = dic.word_set.count()
        words = []
        for i in range(min(l, 6)):
            words.append(dic.word_set.get(pk=random.randint(0, l-1)))
    except Word.DoesNotExist:
        raise Http404("Word not existing")
    return render(request, "home.html", {"dic_name": dic.name, "word_list": words})


def index(request):
    return render(request, "index.html", None)
