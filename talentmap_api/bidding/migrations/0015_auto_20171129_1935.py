# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0018_auto_20171128_2006'),
        ('bidding', '0014_auto_20171129_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBidStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft', models.IntegerField(default=0)),
                ('submitted', models.IntegerField(default=0)),
                ('handshake_offered', models.IntegerField(default=0)),
                ('handshake_accepted', models.IntegerField(default=0)),
                ('in_panel', models.IntegerField(default=0)),
                ('approved', models.IntegerField(default=0)),
                ('declined', models.IntegerField(default=0)),
                ('closed', models.IntegerField(default=0)),
                ('bidcycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid_statistics', to='bidding.BidCycle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_statistics', to='user_profile.UserProfile')),
            ],
            options={
                'ordering': ['bidcycle__cycle_start_date'],
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='userbidstatistics',
            unique_together=set([('bidcycle', 'user')]),
        ),
    ]