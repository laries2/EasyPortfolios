# Generated by Django 4.2.7 on 2024-07-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_role_info_detail_role1_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='detail',
            name='portfolio',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
