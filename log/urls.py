from django.urls import path

from log.views import EntryCreate, EntryDetail


app_name = 'log'
urlpatterns = [
    path('create/', EntryCreate.as_view(), name='create'),
    path('<int:entry_id>', EntryDetail.as_view(), name='detail'),
]
