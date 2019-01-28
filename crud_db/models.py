from django.db import models

# Create your models here.
class emp(models.Model):
	name=models.CharField(max_length=20)
	sal=models.IntegerField()
	email=models.EmailField(default='null')