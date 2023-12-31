# Generated by Django 4.2.3 on 2023-07-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_department_remove_cv_dep_alter_cv_purpose_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cv',
            name='gender',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cv',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.purpose'),
        ),
    ]
