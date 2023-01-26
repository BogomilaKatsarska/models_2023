from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
    )
    level = models.CharField(
        max_length=15,
    )
    age = models.IntegerField()
    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    email = models.EmailField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.full_name}'


