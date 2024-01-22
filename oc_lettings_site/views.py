"""Defines **views** for :mod:`oc_lettings_site`."""

from django.shortcuts import render


def index(request):
    """Display the home page (the local template ``index.html``)"""
    return render(request, 'oc_lettings_site/index.html')
