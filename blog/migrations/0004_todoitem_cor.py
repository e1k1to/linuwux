# Generated by Django 5.0 on 2023-12-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_todoitem_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='cor',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]