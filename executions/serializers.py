from rest_framework.serializers import ModelSerializer

from executions.models import Execution, Prediction


class ExecutionSerializer(ModelSerializer):
    class Meta:
        model = Execution
        fields = '__all__'


class PredicionSerializer(ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'