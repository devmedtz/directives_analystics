from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

from .choices import *
from location.models import Region, District

User = get_user_model()
 
class SubjectCombination(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SchoolSubject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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
    ownership = models.CharField(max_length=100, choices=OWNERSHIP, verbose_name='What is School Type')
    school_multicultural = models.CharField(max_length=100, choices=MULTICULTURAL, verbose_name='Is school has multicultural')
    school_location = models.CharField(max_length=100, choices=SCHOOL_LOCATION, verbose_name='Where school located?')
 
    #School Academics - O'level
    curricular_system = models.CharField(max_length=100, choices=CURRICULAR_SYSTEM, verbose_name='What is curricular system use?')
    school_subjects = models.ManyToManyField(SchoolSubject, blank=True)

    #School Academics - A'level
    subject_combination = models.ManyToManyField(SubjectCombination, blank=True)
   

    #school fees
    average_tution_fee = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Average Tution Fee per Year', blank=True, null=True)
    no_fee = models.BooleanField(default=False, verbose_name='School has scholarship or supported by charity (no-fee)?')

    #school location
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    search_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def save(self):
        super().save()
        logo = Image.open(self.logo.path)
        if logo.height > 300 or logo.width > 300:
            output_size = (300, 300)
            logo.thumbnail(output_size)
            logo.save(self.logo.path)


class SearchResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    gender = models.CharField(max_length=100, blank=True, null=True)

    accomodation_type = models.CharField(max_length=100, blank=True, null=True)

    class_size = models.CharField(max_length=100, blank=True, null=True)

    ownership = models.CharField(max_length=100, blank=True, null=True)

    school_multicultural = models.CharField(max_length=100, blank=True, null=True)

    school_location = models.CharField(max_length=100, blank=True, null=True)
 
    curricular_system = models.CharField(max_length=100, blank=True, null=True)

    school_subjects = models.ManyToManyField(SchoolSubject, blank=True)

    subject_combination = models.ManyToManyField(SubjectCombination, blank=True)

    fee_from = models.CharField(max_length=100, blank=True, null=True)
    fee_to = models.CharField(max_length=100, blank=True, null=True)

    no_fee = models.CharField(max_length=100, blank=True, null=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    phone = models.CharField(max_length=14, blank=True, null=True)

    school = models.ManyToManyField(School, blank=True, related_name='schools')


    def __str__(self):
        return str(self.phone)



class ExamResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    school = models.ForeignKey(School, on_delete=models.SET_NULL,null=True)

    year = models.PositiveIntegerField()
    classe = models.PositiveSmallIntegerField(verbose_name='Form:')
    division_one = models.PositiveIntegerField()
    division_two = models.PositiveIntegerField()
    division_three = models.PositiveIntegerField()
    division_four = models.PositiveIntegerField()
    division_zero = models.PositiveIntegerField()

    def __str__(self):
        return str(self.school.name)


class ExamRank(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    school = models.ForeignKey(School, on_delete=models.SET_NULL,null=True)
    classe = models.PositiveSmallIntegerField(blank=True, null=True)

    dv1T = models.PositiveIntegerField(blank=True, null=True)
    dv2T = models.PositiveIntegerField(blank=True, null=True)
    dv3T = models.PositiveIntegerField(blank=True, null=True)
    dv4T = models.PositiveIntegerField(blank=True, null=True)
    dv0T = models.PositiveIntegerField(blank=True, null=True)

    dv1P = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    dv2P = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    dv3P = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    dv4P = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    dv0P = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    total_point = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)


    def __str__(self):
        return self.school.name


class Subscribe(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Full Name")
    phone = models.CharField(max_length=14, help_text='255xxxxxxxxx')

    def __str__(self):
        return self.name