from django.db import models

# Create your models here.

class Banner(models.Model):
    image=models.ImageField(upload_to='banners/')

    class Meta:
        verbose_name = "banner image 1"
        verbose_name_plural = "banner image 1"


class BannerImage(models.Model):
    image=models.ImageField(upload_to='banner_images/')

    class Meta:
        verbose_name = "banner image 2"
        verbose_name_plural = "banner image 2"

class BannerImage3(models.Model):
    image=models.ImageField(upload_to='banner_images/')

    class Meta:
        verbose_name = "banner image 3"
        verbose_name_plural = "banner image 3"

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

    class Meta:
        verbose_name = "About image"
        verbose_name_plural = "About image"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Our_clients(models.Model):
    image=models.ImageField(upload_to='our_clients/')

    class Meta:
        verbose_name = "Our Client"
        verbose_name_plural = "Our Clients"