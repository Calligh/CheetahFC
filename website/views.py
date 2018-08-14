from django.shortcuts import render,get_object_or_404
from website.models import (
	PlayerSlider,CheetahNew,NewsPosters,PlayerOfWeek,InfoBoard,ClothLining,StarReunion,Wallpaper,
	Video,TalentBridgeAdvert,JerseyAdvert,PictureOfWeek,SportsNew,CEOMessage
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
	cloth_lining = ClothLining.objects.order_by('-created_at')[:12]
	clothing_list = []

	# looping through the images
	for cloth in cloth_lining:
		image_path = cloth.cloth_picture.url
		data = dict({ 'src': image_path })

		if data is not None:
			clothing_list.append(data)
		else:
			data = " No cloths Available .."
			clothing_list.append(data)

	# Cheetah Star Reunion here
	star_reunion = StarReunion.objects.order_by('-created_at')[:12]
	star_list = []

	for star_item in star_reunion:
		image_path = star_item.picture.url
		data = dict({ 'src': image_path })

		if data is not None:
			star_list.append(data)
		else:
			data = " No Star Images Available .." 
			star_list.append(data)

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
		'star_data' : star_list,
		'initials':dat
	}

	return render(request,'website/index.html',context)

def ceoMessage(request):
	msgs = CEOMessage.messages.order_by('-created_at') 
	context = {
		'messages':msgs
	}
	return render(request, 'website/ceomessage.html',context)

def techTeam(request):
	context = {

	}
	return render(request, 'website/teams/technicalteam.html',context)

def firstTeam(request):
	context = {

	}
	return render(request, 'website/teams/firstteam.html',context)

def u17(request):
	context = {

	}
	return render(request, 'website/teams/u17.html',context)

def u15(request):
	context = {

	}
	return render(request, 'website/teams/u15.html',context)

def u13(request):
	context = {

	}
	return render(request, 'website/teams/u13.html',context)