from django.db import models

# Create your models here.


class State_selection(models.Model):
	state_name = models.CharField(max_length=100,primary_key=True)

	def __str__(self):
		return self.state_name

class City_selection(models.Model):
	state_name = models.ForeignKey(State_selection, on_delete=models.CASCADE)
	city_name = models.CharField(max_length =100)

	def __str__(self):
		return self.city_name


