from django.urls import path
from . import views

urlpatterns = [
	path('reserva/', views.home, name='home'),
	path('', views.registro, name="registro"),
	path('crud-empleado/', views.crud_employee, name='crud_employee'),
	path('voucher/', views.voucher, name='voucher')
]