# Generated by Django 2.1 on 2018-08-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20180819_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstteam',
            name='picture',
            field=models.FileField(upload_to='first_team/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='technicalteam',
            name='picture',
            field=models.FileField(upload_to='technical_team/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='u13',
            name='picture',
            field=models.FileField(upload_to='under13/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='u15',
            name='picture',
            field=models.FileField(upload_to='under15/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='u17',
            name='picture',
            field=models.FileField(upload_to='under17/%Y/%m'),
        ),
    ]