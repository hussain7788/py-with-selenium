# Generated by Django 3.0.5 on 2020-05-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
                ('designation', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='employee_photo/')),
                ('langs', models.CharField(max_length=100)),
            ],
        ),
    ]
