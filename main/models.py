from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

from .choices import *
from location.models import Region, District

User = get_user_model()

class School(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    #Basic Information
    name = models.CharField(max_length=200, verbose_name='School Name')
    logo = models.ImageField(upload_to='school_logos/', verbose_name='Upload School Logo')
    gender = models.CharField(max_length=100, choices=GENDER)
    accomodation_type = models.CharField(max_length=100, choices=ACCOMODATION, verbose_name='Accomodation Type')
    class_size = models.CharField(max_length=100, choices=CLASS_SIZE, verbose_name="What is class size")
    school_type = models.CharField(max_length=100, choices=SCHOOL_TYPE, verbose_name='What is School Type')
    school_multicultural = models.CharField(max_length=100, choices=MULTICULTURAL, verbose_name='Is school has multicultural')
    school_location = models.CharField(max_length=100, choices=SCHOOL_LOCATION, verbose_name='Where school located?')

    #School Academics - O'level
    curricular_system = models.CharField(max_length=100, choices=CURRICULAR_SYSTEM, verbose_name='What is curricular system use?')
    school_subjects = MultiSelectField(max_length=100, choices=SCHOOL_SUBJECTS)

    #School Academics - A'level
    subject_combination = MultiSelectField(max_length=100, choices=SUBJECT_COMBINATION)
   

    #school fees
    minimum_tution_fee = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Minimum Tution Fee per Year')
    maximum_tution_fee = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Maximum Tution Fee per Year')
    no_fee = models.BooleanField(default=False, verbose_name='School has scholarship or supported by charity (no-fee)?')

    #school location
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def save(self):
        super().save()
        logo = Image.open(self.logo.path)
        if logo.height > 300 or logo.width > 300:
            output_size = (300, 300)
            logo.thumbnail(output_size)
            logo.save(self.logo.path)


class SchoolExamResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    school = models.ForeignKey(School, on_delete=models.SET_NULL,null=True)
    year = models.PositiveIntegerField()
    division_one = models.PositiveSmallIntegerField()
    division_two = models.PositiveSmallIntegerField()
    division_three = models.PositiveSmallIntegerField()
    division_four = models.PositiveSmallIntegerField()
    division_zero = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.school.name)
