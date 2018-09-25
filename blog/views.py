from django.shortcuts import render
from .models import Post
from django.http import *
from django.template import loader


def index(request):
    return HttpResponse("this is homepage")

