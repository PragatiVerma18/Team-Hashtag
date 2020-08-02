# Generated by Django 3.0.8 on 2020-08-02 15:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('last_date', models.DateTimeField()),
                ('company_name', models.CharField(max_length=100)),
                ('vacancies', models.IntegerField(default=1)),
                ('doc_url', models.URLField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('qualification', models.TextField(blank=True)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('age_limit', models.CharField(default='age >18', max_length=500)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('filled', models.BooleanField(default=False)),
                ('salary', models.IntegerField(blank=True, default=0)),
                ('tags', models.TextField(default='')),
                ('job_for_women', models.BooleanField(default=False, null=True)),
                ('job_for_disabled', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User', to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='Applied', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='profiles.EmployeeProfile', to_field='user')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobs.Job')),
            ],
        ),
    ]
