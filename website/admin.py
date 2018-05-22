from django.contrib import admin
from website.models import PlayerSlider,CheetahNew,NewsPosters
# Register your models here.
class AdminPlayersImages(admin.ModelAdmin):
	list_display = ('players_image','caption')
	search_fields = ('created_at','image_title')

class AdminCheetahNews(admin.ModelAdmin):
	list_display = ('preview_image','headlines')
	search_fields = ('headlines','created_at')

class AdminNewsPoster(admin.ModelAdmin):
	list_display = ('cheetah_news','associate_images')



admin.site.register(PlayerSlider,AdminPlayersImages)
admin.site.register(CheetahNew,AdminCheetahNews)
admin.site.register(NewsPosters,AdminNewsPoster)