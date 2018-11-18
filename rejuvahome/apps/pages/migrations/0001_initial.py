# Generated by Django 2.1.3 on 2018-11-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('pinterest_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]