# Generated by Django 3.1.5 on 2021-03-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_examrank_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='subject_combination',
            field=models.ManyToManyField(blank=True, to='main.SubjectCombination'),
        ),
    ]
