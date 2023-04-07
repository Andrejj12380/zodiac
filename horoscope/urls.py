from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign>', views.get_info_int),
    path('<str:sign>', views.get_info),
]
