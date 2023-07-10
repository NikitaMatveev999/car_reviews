from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=False)

    def __str__(self):
        return self.comment
