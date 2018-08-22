from django.contrib import admin
from website.models import (
    PlayerSlider, CheetahNew, NewsPosters, PlayerOfWeek, InfoBoard, ClothLining, StarReunion, Wallpaper,
    Video, TalentBridgeAdvert, JerseyAdvert, PictureOfWeek, SportsNew, CEOMessage, TechnicalTeam, FirstTeam,
    U13, U15, U17, PlayersAbroad, Gallery
)


# Register your models here.
class AdminPlayersImages(admin.ModelAdmin):
    list_display = ('caption', 'players_image', 'created_at')
    search_fields = ('created_at', 'image_title')


class AdminCheetahNews(admin.ModelAdmin):
    list_display = ('headlines', 'preview_image', 'content', 'created_at')
    search_fields = ('headlines', 'created_at')


class AdminNewsPoster(admin.ModelAdmin):
    list_display = ('cheetah_news', 'associate_images', 'created_at')


class AdminPlayerOfWeek(admin.ModelAdmin):
    list_display = ('heading', 'player_pic', 'short_description', 'created_at')
    search_fields = ('heading',)


class AdminInfoBoard(admin.ModelAdmin):
    list_display = ('teams', 'date', 'time', 'venue', 'status', 'created_at')
    search_fields = ('teams', 'venue', 'status')


class AdminClothLining(admin.ModelAdmin):
    list_display = ('cloth_name', 'cloth_picture', 'pub_date', 'created_at')
    search_fields = ('cloth_name', 'pub_date')


class AdminStarReunion(admin.ModelAdmin):
    list_display = ('caption', 'picture', 'created_at')
    search_fields = ('caption', 'created_at')


class AdminWallpaper(admin.ModelAdmin):
    list_display = ('wallpaper_image', 'wallpaper_caption', 'created_at')
    search_fields = ('wallpaper_caption', 'created_at')


class AdminVideo(admin.ModelAdmin):
    list_display = ('video', 'created_at')
    search_fields = ('created_at',)


class AdminTalentBridgeAdvert(admin.ModelAdmin):
    list_display = ('ad_image', 'ad_caption', 'created_at')
    search_fields = ('created_at', 'ad_image', 'ad_caption')


class AdminPictureOfWeek(admin.ModelAdmin):
    list_display = ('heading', 'picture', 'short_description', 'created_at')
    search_fields = ('created_at', 'heading', 'picture')


class AdminJerseyAdvert(admin.ModelAdmin):
    list_display = ('jersey_image', 'jersey_caption', 'created_at')
    search_fields = ('created_at',)


class AdminSportNew(admin.ModelAdmin):
    list_display = ('preview_image', 'headlines', 'pub_date', 'created_at')
    search_fields = ('headlines', 'pub_date', 'created_at')


class AdminCEOMsg(admin.ModelAdmin):
    list_display = ('ceo_image', 'ceo_message_title', 'ceo_message')
    search_fields = ('ceo_message', 'ceo_message_title')


class AdminTechnicalTeam(admin.ModelAdmin):
    list_display = ('player_name', 'picture', 'profile')
    search_fields = ('player_name',)


class AdminFirstTeam(admin.ModelAdmin):
    list_display = ('player_name', 'picture', 'profile')
    search_fields = ('player_name',)


class AdminU17(admin.ModelAdmin):
    list_display = ('player_name', 'picture', 'profile')
    search_fields = ('player_name',)


class AdminU15(admin.ModelAdmin):
    list_display = ('player_name', 'picture', 'profile')
    search_fields = ('player_name',)


class AdminU13(admin.ModelAdmin):
    list_display = ('player_name', 'picture', 'profile')
    search_fields = ('player_name',)


class AdminPlayersAbroad(admin.ModelAdmin):
    list_display = ('picture', 'player_name', 'profile')
    search_fields = ('player_name',)


admin.site.register(PlayerSlider, AdminPlayersImages)
admin.site.register(CheetahNew, AdminCheetahNews)
admin.site.register(NewsPosters, AdminNewsPoster)
admin.site.register(PlayerOfWeek, AdminPlayerOfWeek)
admin.site.register(InfoBoard, AdminInfoBoard)
admin.site.register(ClothLining, AdminClothLining)
admin.site.register(StarReunion, AdminStarReunion)
admin.site.register(Wallpaper, AdminWallpaper)
admin.site.register(Video, AdminVideo)
admin.site.register(TalentBridgeAdvert, AdminTalentBridgeAdvert)
admin.site.register(PictureOfWeek, AdminPictureOfWeek)
admin.site.register(SportsNew, AdminSportNew)
admin.site.register(JerseyAdvert, AdminJerseyAdvert)
admin.site.register(CEOMessage, AdminCEOMsg)
admin.site.register(TechnicalTeam, AdminTechnicalTeam)
admin.site.register(FirstTeam, AdminFirstTeam)
admin.site.register(U17, AdminU17)
admin.site.register(U15, AdminU15)
admin.site.register(U13, AdminU13)
admin.site.register(PlayersAbroad, AdminPlayersAbroad)
