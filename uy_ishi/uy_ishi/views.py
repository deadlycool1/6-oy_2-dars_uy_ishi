from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def profile(request):
    return render(request, 'profile.html')


def hello(request):
    return HttpResponse("Salom! Django saytimizga xush kelibsiz.")


def information(request):
    return HttpResponse("Bu sayt Django framework yordamida yaratildi.")


def student(request):
    return HttpResponse("Talaba: Shexroz")


def course(request):
    return HttpResponse("Kurs: Backend Python Django")


def message(request):
    return HttpResponse("Django o'rganish juda qiziqarli!")