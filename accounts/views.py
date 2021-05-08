from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . filters import HotelFilter

def states(request):
    state = State.objects.all()
    state_count = state.count()
    hotels = createHotel.objects.all()
    hotels_count = hotels.count()
    myFilter = HotelFilter(request.GET,queryset=hotels)
    hotel = myFilter.qs
    context = {'hotel':hotel,'state_count':state_count,'hotels_count':hotels_count,'myFilter':myFilter,'hotel':hotel}
    return render(request,'accounts/dashboard.html',context)

def about(request):
    return HttpResponse('About')

