# Generated by Django 4.1 on 2022-09-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=True, upload_to='img/%Y/%m/%d/'),
        ),
    ]