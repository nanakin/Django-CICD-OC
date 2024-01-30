"""Views for profiles app."""

from django.shortcuts import render
from .models import Profile

import logging


logger = logging.getLogger()


def index(request):
    """Display a list of :class:`profiles.Profile`.

    Template: ``profiles/index.html``
    """
    logger.info('accessing profiles index')
    profiles_list = Profile.objects.all()
    if len(profiles_list) == 0:
        logger.warning('No profile found')
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Display an individual :class:`profiles.Profile`.

    Template: ``profiles/profile.html``
    """
    logger.info('accessing profile page', extra=dict(username=username))
    profile = Profile.objects.get(user__username=username)
    # no need to catch DoesNotExist exception, it is already
    # - handled by the framework to produce 404
    # - logged and sent to sentry thanks to DjangoIntegration
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
