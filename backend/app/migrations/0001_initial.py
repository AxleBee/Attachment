# Generated by Django 3.2.16 on 2023-01-10 07:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('updated_profile', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('organisation', models.CharField(max_length=255)),
                ('postion', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('photo_url', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('admission_no', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('photo_url', models.ImageField(upload_to='images/')),
                ('assessed_by_employer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('postion', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('photo_url', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('attachment_name', models.CharField(max_length=100)),
                ('department_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('activity', models.CharField(max_length=1000)),
                ('status', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('logbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.logbook')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supervisor')),
            ],
        ),
    ]
