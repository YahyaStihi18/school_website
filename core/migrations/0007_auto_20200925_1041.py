# Generated by Django 3.1.1 on 2020-09-25 09:41

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20200924_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(upload_to='video', validators=[core.validators.validate_file_extension]),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='video', validators=[core.validators.validate_document_extension])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]