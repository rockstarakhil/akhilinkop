import django_filters

from . models import * 

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = createHotel
        fields = 'state','cost','rating'