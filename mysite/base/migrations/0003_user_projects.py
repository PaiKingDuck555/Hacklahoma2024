# Generated by Django 5.0.2 on 2024-02-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_subproject_largeproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='projects', to='base.largeproject'),
        ),
    ]
