# Generated by Django 4.2.3 on 2023-07-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('mob', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('dep', models.CharField(choices=[('Computer science', 'Computer science'), ('Science', 'Science'), ('Commerce', 'Commerce'), ('Humanities', 'Humanities'), ('VHSE', 'VHSE')], max_length=100)),
                ('course', models.CharField(choices=[], max_length=100)),
                ('purpose', models.CharField(choices=[], max_length=100)),
                ('materials', models.CharField(max_length=100)),
            ],
        ),
    ]
