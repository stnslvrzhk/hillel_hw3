# Generated by Django 3.2.3 on 2021-06-14 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logs',
            new_name='Log',
        ),
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['timestamp', 'method']},
        ),
    ]
