from django.db import models

# Create your models here.

class Banner(models.Model):
    image=models.ImageField(upload_to='banners/')

class BannerImage(models.Model):
    image=models.ImageField(upload_to='banner_images/')

class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class About_image(models.Model):
    image=models.ImageField(upload_to='about_images/')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name