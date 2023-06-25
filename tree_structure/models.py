from django.db import models
from django.core.validators import RegexValidator

class TopManager(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 1: Top managers"

class Director(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)
    head = models.ForeignKey(TopManager, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 2: Directors"

class RegionalManager(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)
    head = models.ForeignKey(Director, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 3: Regional managers"

class DistrictManager(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)
    head = models.ForeignKey(RegionalManager, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 4: District managers"

class Teamlead(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)
    head = models.ForeignKey(DistrictManager, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 5: Teamleads"

class Specialist(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)
    head = models.ForeignKey(Teamlead, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 6: Specialists"

class Trainee(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True)
    employment_date = models.DateField(max_length=10)
    head = models.ForeignKey(Specialist, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position} {self.name[0]}.{self.surname}'

    class Meta:
        ordering = ('position', 'surname', 'name')
        verbose_name_plural = "Level 7: Trainees"