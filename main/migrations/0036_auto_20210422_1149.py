# Generated by Django 3.1.5 on 2021-04-22 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20210422_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='accomodation_type',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='class_size',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='curricular_system',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='district',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='fee_from',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='fee_to',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='no_fee',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='ownership',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='region',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='school',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='school_location',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='school_multicultural',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='school_subjects',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='subject_combination',
        ),
    ]