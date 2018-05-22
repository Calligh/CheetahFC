from django.shortcuts import render,get_object_or_404
from website.models import PlayerSlider,CheetahNew
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
	news = CheetahNew.news.order_by('created_at')

	context = {
		'sliders':slider_list,
		'news':news
	}

	return render(request,'website/index.html',context)

def ceoMessage(request):
	context = {
		'data':"Message Title"
	}
	return render(request, 'website/ceomessage.html',context)