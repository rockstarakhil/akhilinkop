from django.db import models

class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class createHotel(models.Model):
    state = models.ForeignKey(State,null=True,on_delete=models.SET_NULL)
    hotelcode = models.CharField(max_length=25)
    cost = models.FloatField(null=False)
    rating = models.FloatField(null=False)

    def __str__(self):
        return self.hotelcode

