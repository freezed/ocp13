from django.urls import include, path

from user import views as user_views

app_name = 'user'
urlpatterns = [
    path('', user_views.index, name='index'),
]
