# Generated by Django 3.1.7 on 2021-03-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_bills_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]