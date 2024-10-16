# Generated by Django 5.1.1 on 2024-10-14 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_alter_model_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalspaces',
            name='model_path',
        ),
        migrations.CreateModel(
            name='RentalSpaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rental_spaces/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myApp.rentalspaces')),
            ],
        ),
    ]
