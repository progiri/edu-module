from django.db import models
from django.utils import timezone

STATUS_CHOICES = [
    (1, 'ToDo'),
    (2, 'InProgress'),
    (3, 'Complete')
]


class ToDo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Task name'
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES
    )
    created_date = models.DateTimeField(
        verbose_name='Created date',
        default=timezone.now
    )

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self) -> str:
        return self.title
