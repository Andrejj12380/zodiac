from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_h),
    path('<int:sign>', views.get_info_int),
    path('<str:sign>', views.get_info, name='horoscope-name'),
    path('types', views.get_types, name='type-name'),
    path('<str:type_>', views.get_info_type),
]
