# Generated by Django 5.0.2 on 2024-02-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_todoitem_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideation',
            name='prompt',
            field=models.CharField(max_length=500, null=True),
        ),
    ]