from django.db import models

# Create your models here.


class hit(models.Model):
	no=models.IntegerField(default=0)
	name=models.CharField(max_length=100)


	def __str__(self):
		return self.name

