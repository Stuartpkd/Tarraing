# Generated by Django 3.2.20 on 2023-08-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brush_app', '0008_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
