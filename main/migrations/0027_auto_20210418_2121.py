# Generated by Django 3.1.5 on 2021-04-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_searchresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='no_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
