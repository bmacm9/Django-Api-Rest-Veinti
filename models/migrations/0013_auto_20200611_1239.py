# Generated by Django 3.0.5 on 2020-06-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
