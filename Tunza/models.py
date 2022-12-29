from django.db import models




# Create your models here.
class Msgs(models.Model):
	email=models.EmailField(max_length=100)
	subject=models.TextField(max_length=50)
	message=models.TextField(max_length=1000)


