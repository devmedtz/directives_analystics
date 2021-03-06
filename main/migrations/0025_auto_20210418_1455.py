# Generated by Django 3.1.5 on 2021-04-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='search_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='school',
            name='average_tution_fee',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='Average Tution Fee per Year'),
        ),
    ]
