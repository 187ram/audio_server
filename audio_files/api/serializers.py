from rest_framework import serializers

from audio_files.models import Audiobook, Podcast, Song


class AudiobookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Audiobook
		fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Podcast
		fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = '__all__'




