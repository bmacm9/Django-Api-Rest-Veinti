# Generated by Django 3.0.5 on 2020-05-17 16:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_commentprofile_hasanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.User')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('commentPhoto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.CommentPhoto')),
                ('commentProfile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.CommentProfile')),
                ('commentStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.CommentStatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.User')),
            ],
        ),
    ]