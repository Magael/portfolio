# Generated by Django 3.2.9 on 2021-11-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='certificates'),
        ),
    ]
