from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
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

    # Var char(50) => strings with max length 50
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level',
    )

    age = models.IntegerField(
        default=-7,
    )

    # int > 0
    years_of_experience = models.PositiveIntegerField()

    # Text => strings with unlimited length
    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField(
        # Adds `UNIQUE` constraint
        unique=True,
        editable=False,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    # This will be automatically set on creation (insert)
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    # This will be automatically set on each `save`/`update`
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )

    # One-to-many
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    # Many-to-many
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # self.id == self.pk
        return f'Id: {self.pk}; Name: {self.fullname}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


# Employee.objects.raw('SELECT * ')  # raw SQL
# Employee.objects.all()  # Select
# Employee.objects.create()  # Insert
# Employee.objects.filter()  # Select + Where
# Employee.objects.update()  # Update

'''
Django ORM (Object-relational mapping)
'''


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

# CASCADE   -    Aко изтрием DEPARTMENT, трябва да изтрием всички Employees
# SET NULL  -    Aко изтрием конкертен DEPARTMENT, трябва да сет-нем NULL в колонката на всчики Employees, които са били в този DEPARTMENT
# SET NULL works only if you set NULL = True in the field
# RESTRICT  -    Не можеш да изприеш DEPARTMENT, ако имаш Employees kъм него

