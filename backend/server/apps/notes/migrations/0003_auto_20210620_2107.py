# Generated by Django 3.1.2 on 2021-06-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='canonical_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='chronological_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]