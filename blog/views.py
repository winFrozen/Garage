from django.http import Http404
from django.shortcuts import render
from .models import Feature, Latest

# Create your views here.
def index(request):
    cars = Feature.objects.all()
    late = Latest.objects.all()
    context = {
        "cars": cars,
        "late": late
    }
    return render(request, 'index.html', context=context)
def cardetailView(request):
    try:
        car = Latest.objects.get(id=id)
        context = {
            "car": car
        }
    except car.DoesNotExsist:
        raise Http404("No car found")
    return render(request, "cardetail.html", context=context)
def contact(request):
    return render(request, 'contact.html', context={})

