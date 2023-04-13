from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.FloatConverter, 'cfloat')
register_converter(converters.DateConverter, 'cdate')

urlpatterns = [
    path('<int:month>/<int:day>', views.search_sign, name='search'),
    path('types', views.get_types, name='types'),
    path('types/<str:element>', views.get_info_sign_element, name='element'),
    path('', views.index_h, name='menu'),
    path('<yyyy:sign_dict>', views.get_yyyy_converters),
    path('<int:sign>', views.get_info_int),
    path('<cfloat:sign_dict>', views.get_float_converters),
    path('<cdate:sign_dict>', views.get_date_converters),
    path('<str:sign>', views.get_info, name='horoscope-name'),
]
