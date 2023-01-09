# Generated by Django 4.1.5 on 2023-01-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
            ],
        ),
    ]