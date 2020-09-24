# Generated by Django 3.1.1 on 2020-09-24 17:40

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200923_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(upload_to='video', validators=[core.validators.validate_file_extension]),
        ),
    ]