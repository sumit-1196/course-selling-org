# Generated by Django 3.1.3 on 2021-01-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='serial_no',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='length',
            field=models.FloatField(),
        ),
    ]
