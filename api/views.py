from django.views.generic import ListView

from api.models import Slider


class SliderListView(ListView):
    model = Slider
    template_name = 'sliders/index.html'
    context_object_name = 'images'

    def get_queryset(self):
        """Фильтруем изображения, которые нужно показать"""
        return Slider.objects.filter(show=True)[:5]

    def get_context_data(self, **kwargs):
        """Подсчитываем количество слайдов, которые будем показывать"""
        context = super().get_context_data(**kwargs)
        context['slides'] = min(5, self.get_queryset().count())
        return context
