# Generated by Django 2.0.3 on 2018-05-11 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Taken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_id', models.IntegerField()),
                ('Semester', models.CharField(max_length=100)),
                ('Number_of_credits', models.IntegerField(max_length=5)),
                ('Grade', models.IntegerField(default=0, max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='Player_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='course_taken',
            name='Player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Player'),
        ),
    ]
