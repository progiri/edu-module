from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

STATUS_CHOICES = [
    (1, 'ToDo'),
    (2, 'InProgress'),
    (3, 'Complete')
]

class ToDo(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        related_name='todos',
        verbose_name='ToDo'
    )
    title = models.CharField(
        max_length=1500,
        verbose_name='Task name'
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES
    )
    created_date = models.DateTimeField(
        verbose_name='Created date',
        default=timezone.now()
    )

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self) -> str:
        return self.task_name

    


