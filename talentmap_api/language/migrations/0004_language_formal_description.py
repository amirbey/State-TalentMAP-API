# Generated by Django 2.0.4 on 2018-04-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0003_auto_20180116_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='formal_description',
            field=models.TextField(help_text='The formal description of the language', null=True),
        ),
    ]
