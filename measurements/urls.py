from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('get/<int:id>', views.get_thisMeasurement, name='get'),
    path('delete/<int:id>', views.delete_thisMeasurement, name='delete'),
    path('form_update/', views.form_update),
    path('update/', views.update_thisMeasurement)
]