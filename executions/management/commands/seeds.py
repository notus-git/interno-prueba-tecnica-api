import random
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand, CommandError

from executions.models import Execution, Prediction


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        self.stdout.write(f"Creando ejecuciones y predicciones...")
        number_of_executions = 10
        seed_start = datetime.today().date() + relativedelta(days=-5)

        # Crear ejecuciones ejecutadas
        for i in range(0, number_of_executions):
            # crear execution
            exec_start = seed_start + relativedelta(days=i)
            exec = Execution.objects.create(
                name=f"ejecución {i}",
                status='Ejecutado',
                start_date= exec_start
            )
            # crear 10 predictions
            for i in range(0, 10):
                prediction_date = exec_start + relativedelta(days=i)
                Prediction.objects.create(
                    date=prediction_date,
                    sales=random.randint(100, 500),
                    execution=exec
                )

        # Crear ejecuciones con estado "creado"
        for i in range(0, 5):
            exec_date = seed_start + relativedelta(days=random.randint(0, 10))
            exec = Execution.objects.create(
                name=f"ejecución {number_of_executions + i}",
                start_date=exec_date,
                status="Creado"
            )
            # crear 10 predictions
            for i in range(0, 10):
                prediction_date = exec_start + relativedelta(days=i)
                Prediction.objects.create(
                    date=prediction_date,
                    sales=0,
                    execution=exec
                )

        self.stdout.write(
                self.style.SUCCESS(f"Seeds finalizados")
            )