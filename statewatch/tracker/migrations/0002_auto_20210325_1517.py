# Generated by Django 3.1.7 on 2021-03-25 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='legbodies',
            name='short_state',
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
        migrations.AlterField(
            model_name='legbodies',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.state'),
        ),
    ]
