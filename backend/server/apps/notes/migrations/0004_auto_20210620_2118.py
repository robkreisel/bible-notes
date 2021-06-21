# Generated by Django 3.1.2 on 2021-06-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210620_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='testament',
            field=models.CharField(choices=[('OT', 'Old Testament'), ('NT', 'New Testament')], default='OT', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('HISTORY', 'Historical'), ('PROPHETS', 'Prophetic'), ('POETIC', 'Poetic and Other Writings'), ('PAUL', "Paul's Letters"), ('LETTERS', 'Letters from Others')], default='HISTORY', max_length=12),
        ),
    ]
