# Generated by Django 3.0 on 2022-04-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0044_purchases_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='score_team1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='score_team2',
            field=models.IntegerField(null=True),
        ),
    ]
