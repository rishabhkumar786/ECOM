# Generated by Django 3.2.6 on 2021-12-27 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tilte',
            new_name='title',
        ),
    ]
