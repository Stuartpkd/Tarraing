# Generated by Django 3.2.20 on 2023-08-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brush_app', '0005_auto_20230801_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='saved_brushes',
            field=models.ManyToManyField(related_name='post_saved', to='brush_app.SavedBrush'),
        ),
    ]