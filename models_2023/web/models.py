from django.db import models


class Department(models.Model):
    name = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return f'ID: {self.pk}, NAME: {self.name}'


class Project(models.Model):
    name = models.CharField(
        max_length=10,
    )
    code_name = models.CharField(
        max_length=10,
    )
    deadline = models.DateField()


class Employee(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
    )
    # CHOICES = ('DB', 'what end-user sees')
    level = models.CharField(
        max_length=15,
        choices=LEVELS,
        verbose_name='Seniority',
    )
    age = models.IntegerField(
        default=-1,
    )
    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    email = models.EmailField(
        unique=True,
        editable=False,
    )
    is_full_time = models.BooleanField(
        null=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.full_name}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


# CASCADE   -    Aко изтрием DEPARTMENT, трябва да изтрием всички Employees
# SET NULL  -    Aко изтрием конкертен DEPARTMENT, трябва да сет-нем NULL в колонката на всчики Employees, които са били в този DEPARTMENT
# SET NULL works only if you set NULL = True in the field
# RESTRICT  -    Не можеш да изприеш DEPARTMENT, ако имаш Employees kъм него

