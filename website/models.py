from django.utils import timezone
from django.db import models

# Create your models here.
class PlayerSlider(models.Model):
	image_name = models.CharField(max_length=30,default='')
	players_image = models.FileField(upload_to='uploads/')
	caption = models.TextField(max_length=50,default= '',blank=True)
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
	cheetah_news = models.ForeignKey(CheetahNew,on_delete=models.CASCADE)
	associate_images = models.FileField(upload_to='associate/')
	created_at = models.DateTimeField(auto_now=True)

