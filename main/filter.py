import django_filters
from .models import School, SubjectCombination
from django import forms
from .choices import *

SCHOOL_SUBJECTS = (
    ('Business-based subjects', 'Business-based subjects'),
    ('Science-based subjects', 'Science-based subjects'),
    ('Nutrition', 'Nutrition'),
    ('Agriculture', 'Agriculture'),
    ('Computer science', 'Computer science'),
    ('Fine Art', 'Fine Art'),
    ('Physical/Sports education', 'Physical/Sports education'),
    ('Music', 'Music'),
)

GENDER = (
    ('Boys', 'Boys'),
    ('Girls', 'Girls'),
    ('co-ed/boys and girls', 'co-ed/boys and girls'),
)

class SchoolFilter(django_filters.FilterSet):

    subject_combination = django_filters.filters.ModelMultipleChoiceFilter(queryset=SubjectCombination.objects.all(), widget=forms.CheckboxSelectMultiple)

    gender = django_filters.filters.ChoiceFilter(choices=GENDER, widget=forms.RadioSelect(attrs={'class': 'inline'}))

    average_tution_fee = django_filters.NumberFilter()

    fee_from = django_filters.NumberFilter(field_name='average_tution_fee', lookup_expr='gt')

    fee_to = django_filters.NumberFilter(field_name='average_tution_fee', lookup_expr='lt')

    class Meta:
        model = School
        exclude = ['logo','created_at','modified_at','created_by','name',]