from django.db import models


class FibNum(models.Model):
    num = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.num}'
