# Generated by Django 5.0.7 on 2024-07-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('want_to_read', 'Want to Read'), ('currently_reading', 'Currently Reading'), ('read', 'Read')], default='want_to_read', max_length=20),
        ),
    ]
