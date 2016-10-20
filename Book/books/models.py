from django.db import models

# Create your models here.


class Publisher(models.Model):
    """Summary

    Attributes:
        address (TYPE): Description
        city (TYPE): Description
        country (TYPE): Description
        name (TYPE): Description
        state_provice (TYPE): Description
        website (TYPE): Description
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_provice = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    """Summary

    Attributes:
        email (TYPE): Description
        first_name (TYPE): Description
        last_name (TYPE): Description
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + '.' + self.last_name


class Book(models.Model):
    """Summary

    Attributes:
        authors (TYPE): Description
        publication_data (TYPE): Description
        publisher (TYPE): Description
        title (TYPE): Description
    """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_data = models.DateField()

    def __str__(self):
        return self.title


class Getdata(object):
    """docstring for ClassName"""
    List = []

    def __init__(self, ob):
        for e in ob.objects.all():
            self.List.append(e.__dict__)
