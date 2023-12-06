from django.db import models

# Create your models here.
class employees (models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    salary=models.IntegerField()
    city=models.CharField(max_length=10)

    def __str__(self):
        return self.name