# Generated by Django 2.1.1 on 2019-03-01 14:05

import Questions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=Questions.models.upload_image_path)),
                ('correct_ans', models.CharField(max_length=500)),
                ('top_level', models.IntegerField(default=34)),
                ('line', models.BooleanField(default=False)),
                ('file_check', models.BooleanField(default=False)),
            ],
        ),
    ]