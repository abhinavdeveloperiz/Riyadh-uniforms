from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Banner, BannerImage, BannerImage3,Service, Gallery,About_image,Contact,Our_clients
# Create your views here.


def Home(request):
    banner = Banner.objects.order_by('-id').first()
    banner_image = BannerImage.objects.order_by('-id').first()
    banner_image3 = BannerImage3.objects.order_by('-id').first()
    services = Service.objects.all()
    gallery = Gallery.objects.all()
    about = About_image.objects.order_by('-id').first()
    clients=Our_clients.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    context = {
        'banner': banner,
        'banner_image': banner_image,
        'banner_image3': banner_image3,
        'services': services,
        'gallery': gallery,
        'about': about,
        'clients':clients,
    }
    return render(request, 'index.html', context)

