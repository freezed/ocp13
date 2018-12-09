from django.urls import include, path

from user import views as user_views

urlpatterns = [
    path('', user_views.index, name='user-index'),
]
