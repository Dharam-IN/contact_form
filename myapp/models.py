from django.db import models

# Create your models here.
class StudentForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    street_address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    class Meta:
        db_table="student_data"

