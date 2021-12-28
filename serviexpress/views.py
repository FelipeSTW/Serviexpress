from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, response
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError

from . forms import CustomUserCreationForm
from . models import Employee, Reservation

import json

def home(request):
	if request.method == 'POST':
		decoded_response = json.loads(request.body)
		try:
			reservation = Reservation.objects.create(
								user=request.user,
								name=decoded_response['name'],
								phone=decoded_response['phone'],
								reservation=decoded_response['date']+ '/' +decoded_response['time']+ '/' +decoded_response['service'],
								# date=decoded_response['date'],
								# time=decoded_response['time'],
								# service=decoded_response['service']
							)
			response_json = {
				'id': reservation.id,
				'name': reservation.name,
				'phone': reservation.phone,
				'reservation': reservation.reservation,
				'msg': 'Hora reservada correctamente!'
			}
		except IntegrityError as e:
			print(e)
			response_json = {
				'msg': 'La hora ya ha sido reservada previamente!'
			}
			return HttpResponse(json.dumps(response_json))
		return HttpResponse(json.dumps(response_json))
	return render(
					request,
					template_name='serviexpress/home.html'
				)
def registro(request):
    context = {
    				'form': CustomUserCreationForm()
    		}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
            				username=formulario.cleaned_data["username"], 
            				password=formulario.cleaned_data["password1"]
            				)
            login(request, user)
            messages.success(request,"Te has registrado exitosamente")
            return redirect(to="home")
        context["form"] = formulario
    return render(
    				request, 
    				template_name='serviexpress/registro.html', 
    				context=context
    			)

def crud_employee(request):
	if request.method == 'POST':
		decoded_response = json.loads(request.body)
		employee = Employee.objects.filter(rut=decoded_response['rut'])
		print(employee)
		employee_exist = employee.exists()
		if employee_exist:
			employee = Employee.objects.update(
												rut=decoded_response['rut'],
												name=decoded_response['name'],
												last_name=decoded_response['last-name'],
												email=decoded_response['email'],
												user_name=decoded_response['username'],
											)
			print(employee)
			response_json = {
			'status': 'Usuario actualizado correctamente'
			}
			return HttpResponse(json.dumps(response_json))
		employee = Employee.objects.create(
									rut=decoded_response['rut'],
									name=decoded_response['name'],
									last_name=decoded_response['last-name'],
									email=decoded_response['email'],
									user_name=decoded_response['username'],
								)
		print(employee)
		response_json = {
			'status': 'Usuario agregado correctamente'
		}
		return HttpResponse(json.dumps(response_json))
	if request.method == 'PUT':
		decoded_response = json.loads(request.body)
		employee = Employee.objects.get(id=decoded_response['id'])
		response_json = {
			'name': employee.name,
			'last-name': employee.last_name,
			'rut': employee.rut
		}
		return HttpResponse(json.dumps(response_json))
	if request.method == 'DELETE':
		decoded_response = json.loads(request.body)
		employee = Employee.objects.get(id=decoded_response['id']).delete()
		response_json = {
			'status': 'Usuario correctamente eliminado'
		}
		return HttpResponse(json.dumps(response_json))
	employees = Employee.objects.all()
	context = {}
	context['employees'] = employees
	return render(
					request,
					template_name='serviexpress/crud-empleado-felipe.html',
					context=context
				)

def voucher(request):
	return render(
		request,
		template_name='serviexpress/voucher.html')