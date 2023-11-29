# Generated by Django 4.2.7 on 2023-11-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_password1_user_password_remove_user_password2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
