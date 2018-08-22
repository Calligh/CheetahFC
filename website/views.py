from django.shortcuts import render, get_object_or_404
from website.models import (
    PlayerSlider, CheetahNew, NewsPosters, PlayerOfWeek, InfoBoard, ClothLining, StarReunion, Wallpaper,
    Video, TalentBridgeAdvert, JerseyAdvert, PictureOfWeek, SportsNew, CEOMessage, TechnicalTeam, FirstTeam,
    U13, U15, U17
)


# Create your views here.

def home(request):
    """
    :param request:
    :return: mixed
    """
    # sliders for the carousel
    sliders = PlayerSlider.sliders.all()
    slider_list = []
    # looping through the images
    for slider in sliders:
        image_path = slider.players_image.url
        data = dict({'src': image_path})

        if data is not None:
            slider_list.append(data)
        else:
            data = " No Images Are Available .."
            slider_list.append(data)

    # news list here
    news = CheetahNew.news.order_by('-created_at')[:9]
    news_total = news.count()

    # player of the week with details
    weekly_player = PlayerOfWeek.objects.order_by('-created_at')[:1]

    # info board data
    information_board = InfoBoard.info_board.order_by('-created_at')[:2]
    # Spliting the teams for some magic events
    # split_title = [team_data.teams.upper().split('VRS') for team_data in information_board if team_data is not None]
    # data = [i[0].strip()[0] for i in split_title if i is not None]
    # data1 = [i[1].strip()[0] for i in split_title if i is not None]
    # dat = [data, data1]

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
        data = dict({'src': image_path})

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
        data = dict({'src': image_path})

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
        data = dict({'src': image_path})

        if data is not None:
            star_list.append(data)
        else:
            data = " No Star Images Available .."
            star_list.append(data)

    # Cheetah Star reunion << Read More >> Here
    star_readMore = StarReunion.objects.order_by('-created_at')
    star_readList = []

    for read_more_item in star_readMore:
        image_path = read_more_item.picture.url
        data = dict({'src': image_path})

        if data is not None:
            star_readList.append(data)
        else:
            data = " No Star Images Available .."
            star_readList.append(data)

    context = {
        'sliders': slider_list,
        'news': news,
        'news_total': news_total,
        'weekly_player': weekly_player,
        'info_board': information_board,
        'weekly_picture': p_of_the_week,
        'jerseys': jersey_advert,
        'wallpapers': wallpaper_list,
        'clothing_lines': cloth_lining,
        'star_data': star_list,
        'star_readmore': star_readList
    }

    return render(request, 'website/index.html', context)


def ceoMessage(request):
    """
    :param request:
    :return: mixed
    """
    msgs = CEOMessage.messages.order_by('-created_at')
    context = {
        'messages': msgs
    }
    return render(request, 'website/ceomessage.html', context)


def techTeam(request):
    """
    :param request:
    :return: mixed
    """
    technical_players = TechnicalTeam.technical_team.order_by('-created_at')
    context = {
        'technical_players': technical_players
    }
    return render(request, 'website/teams/technicalteam.html', context)


def firstTeam(request):
    """
    :param request:
    :return: mixed
    """
    first_players = FirstTeam.first_team.order_by('-created_at')
    context = {
        'first_players': first_players
    }
    return render(request, 'website/teams/firstteam.html', context)


def u17(request):
    """
    :param request:
    :return: mixed
    """
    under17 = U17.objects.order_by('-created_at')
    context = {
        'under17s': under17
    }
    return render(request, 'website/teams/u17.html', context)


def u15(request):
    """
    :param request:
    :return: mixed
    """
    under15 = U15.objects.order_by('-created_at');
    context = {
        'under15': under15
    }
    return render(request, 'website/teams/u15.html', context)


def u13(request):
    """
    :param request:
    :return: mixed
    """
    under13 = U13.objects.order_by('-created_at')
    context = {
        'under13s': under13
    }
    return render(request, 'website/teams/u13.html', context)


def news(request):
    """
    :param request:
    :return: mixed
    """
    news_room = CheetahNew.news.order_by('-created_at')
    context = {
        'news_room': news_room
    }
    return render(request, 'website/news.html', context);


def news_details(request, news_id):
    """
    :param request:
    :param news_id:
    :return: object
    """
    query = get_object_or_404(CheetahNew, pk=news_id)
    posters = NewsPosters.objects.filter(cheetah_news=query.id)
    posters_list = []
    for image in posters:
        image_path = image.associate_images.url
        poster_obj = dict({ 'src' : image_path })

        if poster_obj is not None:
            posters_list.append(poster_obj)
        else:
            poster_obj = "No images available"
            posters_list.append(poster_obj)

    context = {
        'query': query,
        'posters': posters_list
    }
    return render(request, 'website/news_details.html', context)


def fixtures(request):
    """
    :param request:
    :return: mixed
    """
    all_fixtures = InfoBoard.info_board.order_by('-created_at')
    context = {
        'all_fixtures': all_fixtures
    }
    return render(request, 'website/fixtures.html', context)
