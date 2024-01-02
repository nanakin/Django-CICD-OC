from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo con
def index(request):
    return render(request, 'oc_lettings_site/index.html')
