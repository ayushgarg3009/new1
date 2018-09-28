from django.db import models

# Create your models here.

class Post(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20)
	dateofbirth=models.CharField(max_length=20)
	phone=models.IntegerField()
	address=models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name