# Generated by Django 3.1.5 on 2021-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210418_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchresult',
            old_name='average_tution_fee',
            new_name='fee_from',
        ),
        migrations.AddField(
            model_name='searchresult',
            name='fee_to',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True),
        ),
    ]
