from django.urls import include, path

from lead import views as lead_views

urlpatterns = [
    path('', lead_views.index, name='lead-index'),
    path('add/', lead_views.add, name='lead-add'),
    path('<int:contact_id>', lead_views.view, name='lead-view'),
    path('<int:contact_id>/edit/', lead_views.edit, name='lead-edit'),
]
