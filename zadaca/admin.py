from datetime import datetime

from django.contrib import admin
from .models import *
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

class ExhibitAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(ExhibitAdmin, self).get_queryset(request)
        artist = Artist.objects.filter(user=request.user).first()
        if artist:
            aws = Artwork.objects.filter(artist=artist)
            exhibition_ids = aws.values_list('exhibition_id', flat=True)
            return qs.filter(id__in=exhibition_ids)

        if request.user.is_superuser:
            return qs.filter(date_from__gte=datetime.now())

        return qs

class ArtworkAdmin(admin.ModelAdmin):
    exclude = ('artist',)

    def save_model(self, request, obj, form, change):
        artist = Artist.objects.filter(user=request.user).first()
        if artist:
            obj.artist = artist
        return super(ArtworkAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return Artist.objects.filter(user=request.user).first()

    def has_delete_permission(self, request, obj=None):
        artist = Artist.objects.filter(user=request.user).first()
        if obj and artist:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        artist = Artist.objects.filter(user=request.user).first()
        if obj and artist:
            return True
        return False


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Exhibition, ExhibitAdmin)