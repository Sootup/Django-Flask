# Generated by Django 4.1 on 2022-10-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0012_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=None, upload_to='img/%Y/%m/%d/'),
        ),
    ]
