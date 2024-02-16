from django.shortcuts import render


# Create your views here.
def collection(request):
    return render(request, 'collection.html')


def bugatti(request):
    return render(request, 'bugatti.html')


def mclaren(request):
    return render(request, 'mclaren.html')


def rollsroyce(request):
    return render(request, 'rolls royce.html')
