from audio_files.models import Song, Podcast, Audiobook
from django.contrib import admin


# Register your models here.
admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Audiobook)