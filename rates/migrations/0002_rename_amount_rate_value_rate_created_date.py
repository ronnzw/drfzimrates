# Generated by Django 4.2.5 on 2023-09-06 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='amount',
            new_name='value',
        ),
        migrations.AddField(
            model_name='rate',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
