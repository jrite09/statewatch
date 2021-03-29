# Generated by Django 3.1.7 on 2021-03-29 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20210325_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=64)),
                ('sponsor', models.CharField(max_length=64)),
                ('text', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Legislature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.body')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.state')),
            ],
        ),
        migrations.DeleteModel(
            name='LegBodies',
        ),
        migrations.AddField(
            model_name='bills',
            name='legBody',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.legislature'),
        ),
    ]
