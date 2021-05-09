from audio_files.api.serializers import AudiobookSerializer, PodcastSerializer, SongSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from audio_files.models import Audiobook, Podcast, Song



SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'



file_dict = {
	'audiobook' : [Audiobook, AudiobookSerializer],
	'podcast' : [Podcast, PodcastSerializer],
	'song' : [Song, SongSerializer],
}


@api_view(['GET', ])
def api_list_view(request,file_type):
	if file_type not in file_dict:
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		model_class = file_dict[file_type][0]
		model_serializer = file_dict[file_type][1]

	try:
		file = model_class.objects.all()
	except  file_dict[file_type][0].DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = model_serializer(file, many=True)
		return Response(serializer.data)



@api_view(['GET', ])
def api_detail_view(request, file_type, pk):
	
	if file_type not in file_dict:
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		model_class = file_dict[file_type][0]
		model_serializer = file_dict[file_type][1]

	try:
		file = model_class.objects.get(pk = pk)
	except  file_dict[file_type][0].DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = model_serializer(file)
		return Response(serializer.data)



@api_view(['POST'])
def api_create_view(request, file_type):

	if file_type not in file_dict:
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		model_class = file_dict[file_type][0]
		model_serializer = file_dict[file_type][1]

	if request.method == 'POST':
		serializer = model_serializer( data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT',])
def api_update_view(request, file_type, pk):
	
	if file_type not in file_dict:
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		model_class = file_dict[file_type][0]
		model_serializer = file_dict[file_type][1]

	try:
		file = model_class.objects.get(pk=pk)
	except model_class.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = model_serializer(file, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data[SUCCESS] = UPDATE_SUCCESS
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def api_delete_view(request, file_type, pk):

	if file_type not in file_dict:
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		model_class = file_dict[file_type][0]
		model_serializer = file_dict[file_type][1]


	try:
		file = model_class.objects.get(pk=pk)
	except model_class.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		operation = file.delete()
		data = {}
		if operation:
			data[SUCCESS] = DELETE_SUCCESS
		return Response(data=data)