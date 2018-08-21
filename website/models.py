from django.utils import timezone
from django.db import models


# Create your models here.
class PlayerSlider(models.Model):
    image_name = models.CharField(max_length=30, default='')
    players_image = models.FileField(upload_to='uploads/')
    caption = models.TextField(max_length=50, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)

    sliders = models.Manager()


class CheetahNew(models.Model):
    preview_image = models.FileField(upload_to='news/')
    headlines = models.CharField(max_length=50, default='')
    content = models.TextField(max_length=50000, default='')
    pub_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    news = models.Manager()


# Foreign Key table for the cheeta news - that's if there are other pictures to add
class NewsPosters(models.Model):
    cheetah_news = models.ForeignKey(CheetahNew, on_delete=models.CASCADE)
    associate_images = models.FileField(upload_to='associate/')
    created_at = models.DateTimeField(auto_now=True)


# Player of the week database table
class PlayerOfWeek(models.Model):
    heading = models.CharField(max_length=30, default='', blank=True)
    player_pic = models.FileField(upload_to='player_of_week/')
    short_description = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)


# Information Board table for cheeta
SET_SHOW_CHOICES = (
    ('Active', 'ACTIVE'),
    ('Inactive', 'INACTIVE')
)


class InfoBoard(models.Model):
    CH_ACTIVE = 'Active'
    CH_INACTIVE = 'Inactive'
    teams = models.CharField(max_length=300, default='', blank=False, help_text="Team One VRS Team Two")
    date = models.DateField(help_text="Date Of Match")
    time = models.TimeField(help_text="Time Of Match")
    venue = models.CharField(max_length=150, default='', blank=False, help_text="Venue Of Match")
    status = models.CharField(choices=SET_SHOW_CHOICES, max_length=8, default=CH_ACTIVE,
                              help_text="Show Or Hide Info Details")
    score_board_team1 = models.CharField(max_length=2, default='', blank=True, help_text=" Team One Results Here ..")
    score_board_team2 = models.CharField(max_length=2, default='', blank=True, help_text=" Team Two Results Here .. ")
    created_at = models.DateTimeField(auto_now_add=True)

    info_board = models.Manager()


class ClothLining(models.Model):
    cloth_name = models.CharField(max_length=30, default='', blank=True, help_text="Clothing Names (Optional)")
    cloth_picture = models.FileField(upload_to='cloth_lining/')
    cloth_writeup = models.TextField(default='')
    pub_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)


class StarReunion(models.Model):
    picture = models.FileField(upload_to='reunion/')
    caption = models.CharField(max_length=120, default='', blank=True, help_text="Star Reunion ..")
    created_at = models.DateTimeField(auto_now=True)


class Wallpaper(models.Model):
    wallpaper_image = models.FileField(upload_to='wallpapers/')
    wallpaper_caption = models.CharField(max_length=120, default='', blank=True, help_text="Wallpapers Here")
    created_at = models.DateTimeField(auto_now=True)


class TalentBridgeAdvert(models.Model):
    ad_image = models.FileField(upload_to='talent_bridge/%Y/%m/%d/')
    ad_caption = models.CharField(max_length=120, default='', blank=True, help_text="Advert Caption ..")
    created_at = models.DateTimeField(auto_now=True)


class JerseyAdvert(models.Model):
    jersey_image = models.FileField(upload_to='jersey_advert/%Y/%m/%d/')
    jersey_caption = models.CharField(max_length=120, default='', blank=True, help_text="Jersey Caption ..")
    created_at = models.DateTimeField(auto_now=True)


class PictureOfWeek(models.Model):
    heading = models.CharField(max_length=30, default='', blank=True)
    picture = models.FileField(upload_to='player_of_week/')
    short_description = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    video = models.FileField(upload_to='videos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now=True)


class SportsNew(models.Model):
    preview_image = models.FileField(upload_to='news/')
    headlines = models.CharField(max_length=50, default='')
    content = models.TextField(max_length=50000, default='')
    pub_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    sports_news = models.Manager()


# Message from the CEO
class CEOMessage(models.Model):
    ceo_image = models.FileField(upload_to='ceo_pics/', help_text="CEO's Message (Optional)", blank=True)
    ceo_message_title = models.CharField(max_length=500, default='', help_text=" Enter Title Here", blank=True)
    ceo_message = models.TextField(max_length=65535, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)

    messages = models.Manager()


# Technical team model
class TechnicalTeam(models.Model):
    picture = models.FileField(upload_to='technical_team/%Y/%m')
    player_name = models.CharField(max_length=120, default='', help_text="Player Name Here ..")
    profile = models.TextField(max_length=65535, default='', help_text="Some small write up here ..", blank=True)
    created_at = models.DateTimeField(auto_now=True)

    # Custom model manager
    technical_team = models.Manager()


# First Team
class FirstTeam(models.Model):
    picture = models.FileField(upload_to='first_team/%Y/%m')
    player_name = models.CharField(max_length=120, default='', help_text="Player Name Here ..")
    profile = models.TextField(max_length=65535, default='', help_text="Some small write up here ..", blank=True)
    created_at = models.DateTimeField(auto_now=True)

    # Custom model manager
    first_team = models.Manager()


# the Unders Here
class U17(models.Model):
    picture = models.FileField(upload_to='under17/%Y/%m')
    player_name = models.CharField(max_length=120, default='', help_text="Player Name Here ..")
    profile = models.TextField(max_length=65535, default='', help_text="Some small write up here ..", blank=True)
    created_at = models.DateTimeField(auto_now=True)


class U15(models.Model):
    picture = models.FileField(upload_to='under15/%Y/%m')
    player_name = models.CharField(max_length=120, default='', help_text="Player Name Here ..")
    profile = models.TextField(max_length=65535, default='', help_text="Some small write up here ..", blank=True)
    created_at = models.DateTimeField(auto_now=True)


class U13(models.Model):
    picture = models.FileField(upload_to='under13/%Y/%m')
    player_name = models.CharField(max_length=120, default='', help_text="Player Name Here ..")
    profile = models.TextField(max_length=65535, default='', help_text="Some small write up here ..",blank=True)
    created_at = models.DateTimeField(auto_now=True)
