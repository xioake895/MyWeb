from django.db import models

# Create your models here.
class Article(models.Model):
	username=models.CharField(max_length=30)
	passwd=models.TextField()