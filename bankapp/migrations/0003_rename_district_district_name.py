# Generated by Django 3.2.18 on 2023-03-06 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_auto_20230306_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='district',
            new_name='name',
        ),
    ]
