# Generated by Django 4.0.2 on 2022-02-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_room_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=20)),
                ('Comments', models.TextField(max_length=500)),
            ],
        ),
    ]
