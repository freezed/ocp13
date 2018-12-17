from user.views import UserDetail, UserUpdate

from django.urls import path


app_name = 'user'
urlpatterns = [
    path('', UserDetail.as_view(), name='detail'),
    path('edit', UserUpdate.as_view(), name='update'),
]
