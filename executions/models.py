from django.db import models

# Create your models here.


class Execution(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    

class Prediction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()
    sales = models.IntegerField(default=0)
