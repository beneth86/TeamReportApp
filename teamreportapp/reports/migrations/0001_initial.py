# Generated by Django 2.1.2 on 2018-10-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a project name', max_length=255)),
                ('status', models.CharField(blank=True, choices=[('q', 'Queued'), ('i', 'In Progress'), ('c', 'Completed')], default='q', help_text='Project status', max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
