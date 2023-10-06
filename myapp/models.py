from django.db import models

# Create your models here.
class StudentForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=100)

    class Meta:
        db_table="studentdata"

