from django.urls import path

from .views import SliderListView


urlpatterns = [
    path('', SliderListView.as_view(), name='index'),
]
