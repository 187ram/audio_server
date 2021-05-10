from django.urls import path
from audio_files.api.views import(
	api_list_view,
	api_detail_view,
	api_update_view,
	api_delete_view,
	api_create_view,
)

app_name = 'audio_files'

urlpatterns = [
	path('<str:file_type>', api_list_view, name="list"),
	path('<str:file_type>/<int:pk>', api_detail_view, name="detail"),
	path('create/', api_create_view, name="create"),
	path('<str:file_type>/<int:pk>/update', api_update_view, name="update"),
	path('<str:file_type>/<int:pk>/delete', api_delete_view, name="delete"),
]