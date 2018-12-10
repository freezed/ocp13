from django.urls import include, path

from lead import views as lead_views

urlpatterns = [
    path('', lead_views.index, name='lead-index'),
]
