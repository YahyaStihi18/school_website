# Generated by Django 3.1.1 on 2020-11-13 13:23

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201113_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='doc', validators=[core.validators.validate_document_extension]),
        ),
    ]
