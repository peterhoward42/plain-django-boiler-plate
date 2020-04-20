# Generated by Django 3.0.5 on 2020-04-20 07:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('heading_digits', models.CharField(max_length=4, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]{4}$'), 'invalid heading')])),
                ('description', models.CharField(blank=True, max_length=200)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_digits', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]{1,10}$'), 'invalid digits 5,6,7...')])),
                ('description', models.CharField(blank=True, max_length=200)),
                ('indent', models.IntegerField()),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0, 'Negative value not allowed')])),
                ('duty', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0, 'Negative value not allowed')])),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0, 'Negative value not allowed')])),
                ('volume', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0, 'Negative value not allowed')])),
                ('belongs_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tariffs.Heading')),
            ],
        ),
    ]
