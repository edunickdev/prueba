# Generated by Django 4.1.5 on 2023-01-28 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]
