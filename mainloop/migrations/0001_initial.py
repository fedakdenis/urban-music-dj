# Generated by Django 4.0.5 on 2022-07-08 14:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('group', models.CharField(max_length=255)),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]