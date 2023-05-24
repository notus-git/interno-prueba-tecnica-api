from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from executions.models import Execution, Prediction
from executions.serializers import ExecutionSerializer, PredicionSerializer


class ExecutionViewSet(ModelViewSet):
    serializer_class = ExecutionSerializer
    queryset = Execution.objects.all()


class PredictionViewSet(ModelViewSet):
    serializer_class = PredicionSerializer
    queryset = Prediction.objects.all()