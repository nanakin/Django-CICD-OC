"""Views for lettings app."""

from django.shortcuts import render
from .models import Letting

import logging


logger = logging.getLogger()


def index(request):
    """Display list of :class:`lettings.Letting`.

    Template: `lettings/index.html`
    """
    lettings_list = Letting.objects.all()
    logger.info('accessing lettings index')
    if len(lettings_list) == 0:
        logger.warning('No letting found')
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Display an individual :class:`lettings.Letting`.

    Template: `lettings/letting.html`
    """
    logger.info('accessing letting page', extra=dict(letting_id=letting_id))
    letting = Letting.objects.get(id=letting_id)
    # no need to catch DoesNotExist exception, it is already
    # - handled by the framework to produce 404
    # - logged and sent to sentry thanks to DjangoIntegration
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
