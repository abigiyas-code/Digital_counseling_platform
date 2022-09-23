from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to LSSYA! We are here for you!")
