# Generated by Django 5.1.1 on 2024-10-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_model_three_path_delete_rentalspaceimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tenant', 'Tenant'), ('User', 'User')], default='User', max_length=20),
        ),
    ]
