from django.urls import include, path

from lead import views as lead_views

app_name = 'lead'
urlpatterns = [
    path('', lead_views.ContactList.as_view(), name='index'),
    path('add/', lead_views.add, name='add'),
    path('<int:contact_id>', lead_views.ContactDetail.as_view(), name='view'),
    path('<int:contact_id>/edit/', lead_views.edit, name='edit'),
]
