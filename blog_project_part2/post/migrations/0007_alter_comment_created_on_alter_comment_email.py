# Generated by Django 5.0.6 on 2024-07-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]