from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
	rut = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	user_name = models.CharField(max_length=30)

	def __str__(self):
		return self.name + ' ' + self.last_name

class Reservation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, default='')
	phone = models.CharField(max_length=30, default='')
	reservation = models.CharField(max_length=100, default='', unique=True)

	def __str__(self):
		return self.name

# class Reservation(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=30, default='')
# 	phone = models.CharField(max_length=30, default='')
# 	date = models.CharField(max_length=30, default='')
# 	time = models.CharField(max_length=30, default='')
# 	service = models.CharField(max_length=30, default='')

# 	def __str__(self):
# 		return self.name + ' ' + self.service

# class Region(models.Model):
# 	name = models.CharField(max_length=30)

# 	def __str__(self):
# 		return self.name

# class City(models.Model):
# 	name = models.CharField(max_length=30)
# 	region = models.ForeignKey(
# 								Region,
# 								on_delete=models.CASCADE
# 							)
# 	def __str__(self):
# 		return self.name

# 	class Meta:
# 		verbose_name_plural = 'cities'

