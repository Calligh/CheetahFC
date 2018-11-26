# Generated by Django 2.0.3 on 2018-06-10 22:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_clothlining_starreunion_wallpaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='JerseyAdvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jersey_image', models.FileField(upload_to='jersey_advert/%Y/%m/%d/')),
                ('jersey_caption', models.CharField(blank=True, default='', help_text='Jersey Caption ..', max_length=120)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PictureOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, default='', max_length=30)),
                ('picture', models.FileField(upload_to='player_of_week/')),
                ('short_description', models.CharField(blank=True, default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SportsNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview_image', models.FileField(upload_to='news/')),
                ('headlines', models.CharField(default='', max_length=50)),
                ('content', models.TextField(default='', max_length=50000)),
                ('pub_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('sports_news', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TalentBridgeAdvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_image', models.FileField(upload_to='talent_bridge/%Y/%m/%d/')),
                ('ad_caption', models.CharField(blank=True, default='', help_text='Advert Caption ..', max_length=120)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
