from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_thismeasurement
from .logic.logic_measurements import update_thismeasurement
from .logic.logic_measurements import delete_thismeasurement
from django.http import HttpResponse
from django.core import serializers
from.models import Measurement
from django.shortcuts import render

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json',measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_thisMeasurement(request,id):
    measurements = get_thismeasurement(id)
    serialized_obj = serializers.serialize('json', [ measurements, ])
    return HttpResponse(serialized_obj, content_type='application/json')

def delete_thisMeasurement(request,id):
    delete_thismeasurement(id)
    return HttpResponse("borrado")

def form_update(request):
    return render(request,"update_measurements.html")

def update_thisMeasurement(request):
    entrada= request.GET["id"]
    entrada2= request.GET["value"]
    entrada3 = request.GET["unit"]
    entrada4 = request.GET["place"]
    update_thismeasurement(entrada, entrada2, entrada3, entrada4)
    return HttpResponse("actualizado")


