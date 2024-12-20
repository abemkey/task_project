from django.db import models

class Sponsors(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Study(models.Model):
    STUDY_CHOICES = [
        ('P1', 'Phase I'),
        ('P2', 'Phase II '),
        ('P3', 'Phase III'),
        ('P4', 'Phase IV '),
    ]
    study_Name = models.CharField(max_length=50)
    study_Description = models.CharField(max_length=250)
    study_Phase= models.CharField(
        max_length=3,
        choices=STUDY_CHOICES,
        default='P1',
    )
    Sponsor_Name=models.ForeignKey(Sponsors, on_delete=models.DO_NOTHING)

