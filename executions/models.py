from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models

# Create your models here.


class Execution(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    
    def create_empty_predictions(self):
        for i in range(0, 10):
            Prediction.objects.create(
                date=self.start_date + relativedelta(days=i),
                sales=0,
                execution=self
            )


class Prediction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()
    sales = models.IntegerField(default=0)
    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
