# Generated by Django 3.1.5 on 2021-03-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210309_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_subjects',
            field=models.ManyToManyField(blank=True, to='main.SchoolSubject'),
        ),
    ]
