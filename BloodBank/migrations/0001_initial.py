# Generated by Django 3.2.7 on 2021-09-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('phoneno', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('dod', models.DateField()),
            ],
        ),
    ]