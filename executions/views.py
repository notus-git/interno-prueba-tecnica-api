from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from executions.models import Execution, Prediction
from executions.serializers import ExecutionSerializer, PredictionSerializer


class ExecutionViewSet(ModelViewSet):
    serializer_class = ExecutionSerializer
    queryset = Execution.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ExecutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        execution = Execution.objects.create(
            name=serializer.validated_data["name"],
            status=serializer.validated_data["status"],
            start_date=serializer.validated_data["start_date"]
        )
        execution.create_empty_predictions()
        return Response(status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['GET'])
    def get_predictions(self, request, pk=None):
        res = list(Prediction.objects.filter(execution__id=pk).order_by('date').values('id', 'execution', 'sales', 'date'))
        return Response(res)
        

class PredictionViewSet(ModelViewSet):
    serializer_class = PredictionSerializer
    queryset = Prediction.objects.all()