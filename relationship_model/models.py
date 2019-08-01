from django.db import models

# Part 1 

class Country(models.Model):
    name = models.CharField(max_length = 255)
    year_founded = models.IntegerField()
    national_animal = models.CharField(max_length = 255)

class Province(models.Model):
    name = models.CharField(max_length = 255)
    year_founded = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, name= 'country')

class City(models.Model):
    name = models.CharField(max_length = 255)
    year_founded = models.IntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, name= 'province')


class Residence(models.Model):
    address = models.TextField()
    year_built = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, name='city')

class Person(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, name='residence')


# Part 2

class Film(models.Model):
    title = models.CharField(max_length = 255)
    year = models.IntegerField()

class Viewer(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    films_watched = models.ManyToManyField(Film)






