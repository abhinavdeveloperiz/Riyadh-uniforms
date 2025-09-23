from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, BannerImage, Service, Gallery,About_image,Contact

admin.site.site_header = "Riyadh Uniform"
admin.site.site_title = "Riyadh Uniform Admin"
admin.site.index_title = "Welcome to Riyadh Uniform Admin Portal"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "message", "submitted_at")
    list_filter = ("submitted_at",)  # Adds a filter by date in the sidebar
    search_fields = ("name", "phone", "message")  # Optional: search box
    ordering = ("-submitted_at",)  # Show newest first


# Reusable image preview
def image_preview(obj):
    if obj.image:
        return format_html('<img src="{}" width="100" style="border-radius:6px;" />', obj.image.url)
    return "No Image"


@admin.register(About_image)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj)
    image_preview.short_description = "Preview"


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj)
    image_preview.short_description = "Preview"


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj)
    image_preview.short_description = "Preview"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj)
    image_preview.short_description = "Preview"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return image_preview(obj)
    image_preview.short_description = "Preview"






