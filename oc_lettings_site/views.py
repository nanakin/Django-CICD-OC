"""Defines *views* for `oc_lettings_site`."""

from django.shortcuts import render


def index(request):
    """Display the home page.

    Template:
    :template:`'oc_lettings_site/index.html`
    """
    return render(request, 'oc_lettings_site/index.html')
