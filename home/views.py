from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def store(request):
    """ A view to return the index page """

    return render(request, 'home/store.html')
