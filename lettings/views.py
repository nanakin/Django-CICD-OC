from django.shortcuts import render
from .models import Letting

import logging


logger = logging.getLogger()


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
def index(request):
    lettings_list = Letting.objects.all()
    logger.info('accessing lettings index')
    if len(lettings_list) == 0:
        logger.warning('No letting found')
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
def letting(request, letting_id):
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
