import datetime
from django.db import models
from django.db.models import Avg, F


class BirthDayManager(models.Manager):
    def get_average_age(self):
        return self.get_queryset().aggregate(
            average_age=Avg(
                    datetime.date.today() - F('birthday')
                )
            )


class BirthDay(models.Model):
    """
    It's The Birthday model to gather all the user birthday records.
    """
    first_name = models.CharField(max_length=52)
    last_name = models.CharField(max_length=52)
    birthday = models.DateField()
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BirthDayManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.email)

    class Meta:
        ordering = ['-created_at']
        # db_table = 'birth_day'
