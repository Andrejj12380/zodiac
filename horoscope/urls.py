from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>/<int:day>', views.search_sign, name='search'),
    path('types', views.get_types, name='types'),
    path('types/<str:element>', views.get_info_sign_element, name='element'),
    path('', views.index_h, name='menu'),
    path('<int:sign>', views.get_info_int),
    path('<str:sign>', views.get_info, name='horoscope-name'),
]
