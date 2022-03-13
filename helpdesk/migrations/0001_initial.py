# Generated by Django 4.0.3 on 2022-03-12 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('Read', 'Read'), ('All', 'All')], default='All', max_length=4)),
                ('role', models.CharField(choices=[('Author', 'Author'), ('Manager', 'Manager'), ('Creator', 'Creator')], default='Author', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('type', models.CharField(choices=[('backend', 'backend'), ('frontend', 'frontend'), ('Android', 'Android'), ('iOS', 'iOS')], default='backend', max_length=8)),
                ('author_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_user_id_project', to=settings.AUTH_USER_MODEL)),
                ('contributor', models.ManyToManyField(related_name='contributors', through='helpdesk.Contributor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Task', 'Task'), ('Upgrade', 'Upgrade')], default='Bug', max_length=7)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Open', 'Open'), ('Closed', 'Closed')], default='Pending', max_length=7)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_user_id_issue', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_user_id_issue', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.project')),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_id_contributor', to='helpdesk.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id_contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=2048)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_user_id_comment', to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_id_comment', to='helpdesk.issue')),
            ],
        ),
    ]
