# Generated by Django 5.0 on 2023-12-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_todoitem_postzinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postzinho',
            name='texto',
            field=models.TextField(max_length=1000),
        ),
    ]