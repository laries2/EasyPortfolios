# Generated by Django 4.2.7 on 2023-11-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_detail_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='role2_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='role3_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='role_info',
            field=models.TextField(),
        ),
    ]
