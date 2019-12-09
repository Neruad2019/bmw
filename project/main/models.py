from django.db import models
from django.urls import reverse
from django.conf import settings

#Car Category
class Category(models.Model):
    CATEGORY_CHOICE = (('New','New'),('Crossover','Crossover'),('Sport','Sport'),)
    name = models.CharField(max_length = 15, choices = CATEGORY_CHOICE)
    slug = models.SlugField(max_length = 15, unique = True)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


#Car
class Car(models.Model):
    category = models.ForeignKey(Category, default = None, on_delete=models.SET_DEFAULT,)
    name = models.CharField(max_length = 20)
    body = models.TextField()
    power = models.IntegerField()
    volume = models.FloatField()
    max_speed = models.IntegerField()
    acceleration = models.FloatField()
    img = models.ImageField(upload_to = 'car_image', blank = True, null = True)
    price = models.IntegerField(blank = True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.body[:70]+' ...'

    def watt(self):
        return self.power * 0.745
