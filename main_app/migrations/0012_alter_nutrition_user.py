# Generated by Django 3.2.9 on 2021-12-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_nutrition_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
