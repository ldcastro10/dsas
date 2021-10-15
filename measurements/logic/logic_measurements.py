from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_thismeasurement(id):
    measurements = Measurement.objects.get(pk=id)
    return measurements

def delete_thismeasurement(id):
    Measurement.objects.filter(pk=id).delete()

def update_thismeasurement(entrada,entrada2,entrada3,entrada4):
    Measurement.objects.filter(pk=entrada).update(value=entrada2)
    Measurement.objects.filter(pk=entrada).update(unit=entrada3)
    Measurement.objects.filter(pk=entrada).update(place=entrada4)
