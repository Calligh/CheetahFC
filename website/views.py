from django.shortcuts import render,get_object_or_404
from website.models import (
	PlayerSlider,CheetahNew,NewsPosters,PlayerOfWeek,InfoBoard,ClothLining,StarReunion,Wallpaper,
	Video,TalentBridgeAdvert,JerseyAdvert,PictureOfWeek,SportsNew
	)
# Create your views here.

def home(request):
	# sliders for the carousel
	sliders = PlayerSlider.sliders.all()
	slider_list = []
	# looping through the images
	for slider in sliders:
		image_path = slider.players_image.url
		data = dict({ 'src':image_path})

		if data is not None:
			slider_list.append(data)
		else:
			data = " No Images Are Available .."
			slider_list.append(data)

	# news list here
	news = CheetahNew.news.order_by('-created_at')
	news_total = news.count()

	# player of the week with details
	weekly_player = PlayerOfWeek.objects.order_by('-created_at')[:1]

	# info board data
	information_board = InfoBoard.info_board.order_by('-created_at')[:2]
	#Spliting the teams for some magic events
	split_title = [team_data.teams.upper().split('VRS') for team_data in information_board if team_data is not None]
	data = [i[0].strip()[0] for i in split_title if i is not None]
	data1 = [i[1].strip()[0] for i in split_title if i is not None]
	dat = [data,data1]


	# Picture of the week
	p_of_the_week = PictureOfWeek.objects.order_by('-created_at')[:1]
	# Jersey Advert
	jersey_advert = JerseyAdvert.objects.order_by('-created_at')[:1]

	# wallpapers 
	wallpapers = Wallpaper.objects.all()
	wallpaper_list = []
	# looping through the images
	for wallpaper in wallpapers:
		image_path = wallpaper.wallpaper_image.url
		data = dict({ 'src':image_path})

		if data is not None:
			wallpaper_list.append(data)
		else:
			data = " No Images Are Available .."
			wallpaper_list.append(data)

	# Clothing line configs here
	cloth_lining = ClothLining.objects.order_by('-created_at')

	context = {
		'sliders':slider_list,
		'news':news,
		'news_total': news_total,
		'weekly_player': weekly_player,
		'info_board' : information_board,
		'weekly_picture':p_of_the_week,
		'jerseys':jersey_advert,
		'wallpapers':wallpaper_list,
		'clothing_lines':cloth_lining,
		'initials':dat
	}

	return render(request,'website/index.html',context)

def ceoMessage(request):
	context = {
		'data':"Message Title"
	}
	return render(request, 'website/ceomessage.html',context)