# Generated by Django 4.1.3 on 2022-12-10 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auction_date_alter_watclist_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 13, 33, 29, 327940)),
        ),
    ]
