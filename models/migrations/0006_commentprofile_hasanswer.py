# Generated by Django 3.0.5 on 2020-05-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20200503_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentprofile',
            name='hasAnswer',
            field=models.CharField(default='no', max_length=10),
        ),
    ]
