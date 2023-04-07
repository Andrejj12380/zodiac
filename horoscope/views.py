from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
import requests

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
              'https://cdn-icons-mp4.flaticon.com/512/9084/9084119.mp4'],
    'Taurus': ['Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084141.mp4'],
    'Gemini': ['Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084168.mp4'],
    'Cancer': ['Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084442.mp4'],
    'Leo': ['Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)',
            'https://cdn-icons-mp4.flaticon.com/512/9084/9084233.mp4'],
    'Virgo': ['Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)',
              'https://cdn-icons-mp4.flaticon.com/512/9084/9084261.mp4'],
    'Libra': ['Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
              'https://cdn-icons-mp4.flaticon.com/512/9084/9084295.mp4'],
    'Scorpio': ['Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)',
                'https://cdn-icons-mp4.flaticon.com/512/9084/9084322.mp4'],
    'Sagittarius': ['Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)',
                    'https://cdn-icons-mp4.flaticon.com/512/9084/9084322.mp4'],
    'Capricorn': ['Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)',
                  'https://cdn-icons-mp4.flaticon.com/512/9084/9084382.mp4'],
    'Aquarius': ['Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)',
                 'https://cdn-icons-mp4.flaticon.com/512/9084/9084412.mp4'],
    'Pisces': ['Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)',
               'https://cdn-icons-mp4.flaticon.com/512/9084/9084427.mp4'],
}


def get_info(request, sign: str):
    for key, value in sign_dict.items():
        if sign.lower() == key.lower():
            return render(request, 'index.html', {'info': value[0],
                                                  'name': key,
                                                  'text': response_phrase['daily'],
                                                  'video': value[1]})
    else:
        return HttpResponse(f'Нет запрашиваемого знака зодиака {sign}')


def get_info_int(request, sign: int):
    signs_list = list(sign_dict)
    if sign > len(signs_list):
        return HttpResponseNotFound(f'Нет запрашиваемого знака зодиака {sign}')
    sign_name = signs_list[sign - 1]
    return HttpResponseRedirect(f'{sign_name.lower()}')
