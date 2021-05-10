from rest_framework import serializers
from audio_files.models import Audiobook, Podcast, Song


class AudiobookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Audiobook
		fields = ['id', 'name', 'author', 'narrator', 'duration','uploaded_time', ]


class PodcastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Podcast
		fields = ['id', 'name', 'duration', 'host', 'participants', 'uploaded_time',]


class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ['id', 'name', 'duration', 'uploaded_time',]




