# Generated by Django 5.0 on 2023-12-12 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_todoitem_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='completed',
        ),
    ]
