import datetime
import traceback

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
import requests
from django.urls import reverse

URL = "https://horoscope-astrology.p.rapidapi.com"

URL_HOROSCOPE = 'https://rapidapi.com/Alejandro99aru/api/horoscope-astrology'

phrase = '/dailyphrase'

headers = {
    "X-RapidAPI-Key": "8fced68bc2msh3deff88764c013cp19eb68jsn48cf2880a3dc",
    "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
}

response_phrase = requests.request("GET", f'{URL}{phrase}', headers=headers).json()

sign_dict = {
    'Aries': ['Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)',
              'https://cdn-icons-mp4.flaticon.com/512/9084/9084119.mp4', [80, 110]],
    'Taurus': ['Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084141.mp4', [111, 141]],
    'Gemini': ['Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084168.mp4', [142, 172]],
    'Cancer': ['Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084442.mp4', [173, 203]],
    'Leo': ['Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)',
            'https://cdn-icons-mp4.flaticon.com/512/9084/9084233.mp4', [204, 233]],
    'Virgo': ['Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)',
              'https://cdn-icons-mp4.flaticon.com/512/9084/9084261.mp4', [234, 266]],
    'Libra': ['Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
              'https://cdn-icons-mp4.flaticon.com/512/9084/9084295.mp4', [267, 296]],
    'Scorpio': ['Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)',
                'https://cdn-icons-mp4.flaticon.com/512/9084/9084322.mp4', [297, 326]],
    'Sagittarius': ['Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)',
                    'https://cdn-icons-mp4.flaticon.com/512/9084/9084322.mp4', [327, 356]],
    'Capricorn': ['Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)',
                  'https://cdn-icons-mp4.flaticon.com/512/9084/9084382.mp4', [357, 20]],
    'Aquarius': ['Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)',
                 'https://cdn-icons-mp4.flaticon.com/512/9084/9084412.mp4', [21, 50]],
    'Pisces': ['Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084427.mp4', [51, 79]],
}

types_ = {
    'Fire': ['Aries', 'Leo', 'Sagittarius'],
    'Air': ['Gemini', 'Libra', 'Aquarius'],
    'Earth': ['Taurus', 'Virgo', 'Capricorn'],
    'Water': ['Cancer', 'Scorpio', 'Pisces']
}


def get_info(request, sign: str):
    for key, value in sign_dict.items():
        if sign.lower() == key.lower():
            return render(request, 'index.html', {'info': value[0],
                                                  'name': key,
                                                  'text': response_phrase['daily'],
                                                  'video': value[1]}, )
    else:
        return HttpResponse(f'Нет запрашиваемого знака зодиака {sign}')


def get_info_int(request, sign: int):
    signs_list = list(sign_dict)
    if sign > len(signs_list):
        return HttpResponseNotFound(f'Нет знака зодиака под номером {sign}')
    sign_name = signs_list[sign - 1]
    redirect_url = reverse('horoscope-name', args=(sign_name,))
    return HttpResponseRedirect(redirect_url)


def index_h(request):
    signs_list = list(sign_dict)
    res = ''
    for sign in signs_list:
        redirect_url = reverse('horoscope-name', args=(sign,))
        res += f'<li><a href="{redirect_url}">{sign}</a></li>'
    response = f"""
    <ol>
    {res}
    </ol>
    """
    return HttpResponse(response)


def get_types(request):
    types_list = list(types_)
    res = ''
    for type_ in types_list:
        redirect = reverse('element', args=(type_,))
        res += f'<li><a href="{redirect}">{type_}</a></li>'
    response = f"""
        <ol>
        {res}
        </ol>
        """
    return HttpResponse(response)


def get_info_sign_element(request, element: str):
    res = ''
    print(request)
    for sign in types_[element.title()]:
        redirect = reverse('horoscope-name', args=(sign,))
        res += f'<li><a href="{redirect}">{sign}</a></li>'
    response = f"""
            <ol>
            {res}
            </ol>
            """
    return HttpResponse(response)


def search_sign(request, month: int, day: int):
    try:
        datetime.date(year=datetime.date.today().year, month=month, day=day)
    except ValueError as e:
        massage_triger = str(e).split(' ')[0]
        if massage_triger == 'day':
            err = 'Нет такого дня в этом месяце'
            traceback.print_exc()
            return render(request, 'error.html', {'error_message': err})
        elif massage_triger == 'month':
            err = 'Номер месяца должен быть от 1 до 12'
            traceback.print_exc()
            return render(request, 'error.html', {'error_message': err})
        else:
            err = 'Непредвиденная ошибка'
            traceback.print_exc()
            return render(request, 'error.html', {'error_message': err})

    date = datetime.date(year=datetime.date.today().year, month=month, day=day)
    day_number = date.toordinal() - datetime.date(date.year, 1, 1).toordinal() + 1
    try:
        for key, value in sign_dict.items():
            if day_number in range(value[2][0], value[2][1] + 1):
                redirect = reverse('horoscope-name', args=(key,))
                return HttpResponseRedirect(redirect)
        err = 'No horoscope found for this day'
        return HttpResponse(err)
    except Exception as e:
        err = str(e)
        traceback.print_exc()
        return HttpResponse(err)

