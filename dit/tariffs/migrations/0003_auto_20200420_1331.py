# Generated by Django 3.0.5 on 2020-04-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tariffs", "0002_commodity_is_leaf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commodity", name="indent", field=models.IntegerField(default=0),
        ),
    ]