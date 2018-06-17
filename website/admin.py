from django.contrib import admin
from website.models import (
	PlayerSlider,CheetahNew,NewsPosters,PlayerOfWeek,InfoBoard,ClothLining,StarReunion,Wallpaper,
	Video,TalentBridgeAdvert,JerseyAdvert,PictureOfWeek,SportsNew
	)
# Register your models here.
class AdminPlayersImages(admin.ModelAdmin):
	list_display = ('players_image','caption','created_at')
	search_fields = ('created_at','image_title')

class AdminCheetahNews(admin.ModelAdmin):
	list_display = ('preview_image','headlines','created_at')
	search_fields = ('headlines','created_at')

class AdminNewsPoster(admin.ModelAdmin):
	list_display = ('cheetah_news','associate_images','created_at')

class AdminPlayerOfWeek(admin.ModelAdmin):
	list_display = ('heading','player_pic','short_description','created_at')
	search_fields = ('heading',)

class AdminInfoBoard(admin.ModelAdmin):
	list_display = ('teams','date','time','venue','status','created_at')
	search_fields = ('teams','venue','status')

class AdminClothLining(admin.ModelAdmin):
	list_display = ('cloth_name','cloth_picture','pub_date','created_at')
	search_fields = ('cloth_name','pub_date')

class AdminStarReunion(admin.ModelAdmin):
	list_display = ('picture','caption','created_at')
	search_fields = ('caption','created_at')

class AdminWallpaper(admin.ModelAdmin):
	list_display = ('wallpaper_image','wallpaper_caption','created_at')
	search_fields = ('wallpaper_caption','created_at')

class AdminVideo(admin.ModelAdmin):
	list_display = ('video','created_at')
	search_fields = ('created_at',)

class AdminTalentBridgeAdvert(admin.ModelAdmin):
	list_display = ('ad_image','ad_caption','created_at')
	search_fields = ('created_at','ad_image','ad_caption')

class AdminPictureOfWeek(admin.ModelAdmin):
	list_display = ('heading','picture','short_description','created_at')
	search_fields = ('created_at','heading','picture')

class AdminJerseyAdvert(admin.ModelAdmin):
	list_display = ('jersey_image','jersey_caption','created_at')
	search_fields = ('created_at',)

class AdminSportNew(admin.ModelAdmin):
	list_display = ('preview_image','headlines','pub_date','created_at')
	search_fields = ('headlines','pub_date','created_at')

admin.site.register(PlayerSlider,AdminPlayersImages)
admin.site.register(CheetahNew,AdminCheetahNews)
admin.site.register(NewsPosters,AdminNewsPoster)
admin.site.register(PlayerOfWeek,AdminPlayerOfWeek)
admin.site.register(InfoBoard,AdminInfoBoard)
admin.site.register(ClothLining,AdminClothLining)
admin.site.register(StarReunion,AdminStarReunion)
admin.site.register(Wallpaper,AdminWallpaper)
admin.site.register(Video,AdminVideo)
admin.site.register(TalentBridgeAdvert,AdminTalentBridgeAdvert)
admin.site.register(PictureOfWeek,AdminPictureOfWeek)
admin.site.register(SportsNew,AdminSportNew)
admin.site.register(JerseyAdvert,AdminJerseyAdvert)