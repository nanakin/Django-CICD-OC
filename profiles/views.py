from django.shortcuts import render
from .models import Profile

import logging


logger = logging.getLogger()


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed co
def index(request):
    logger.info('accessing profiles index')
    profiles_list = Profile.objects.all()
    if len(profiles_list) == 0:
        logger.warning('No profile found')
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
def profile(request, username):
    logger.info('accessing profile page', extra=dict(username=username))
    profile = Profile.objects.get(user__username=username)
    # no need to catch DoesNotExist exception, it is already
    # - handled by the framework to produce 404
    # - logged and sent to sentry thanks to DjangoIntegration
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
