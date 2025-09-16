from django.shortcuts import render
from .models import Banner, BannerImage, Service, Gallery,About_image
# Create your views here.


def Home(request):
    banner=Banner.objects.order_by('-id').first()
    banner_image=BannerImage.objects.order_by('-id').first()
    services=Service.objects.all()
    gallery=Gallery.objects.all()
    about=About_image.objects.order_by('-id').first()
    context={
        'banner':banner,
        'banner_image':banner_image,
        'services':services,
        'gallery':gallery,
        'about':about,
    }
    return render(request, 'index.html',context)