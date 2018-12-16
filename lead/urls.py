from django.urls import include, path

from lead.views import ContactCreate, ContactDetail, ContactList, ContactUpdate

app_name = 'lead'
urlpatterns = [
    path('', ContactList.as_view(), name='index'),
    path('add/', ContactCreate.as_view(), name='add'),
    path('<int:contact_id>', ContactDetail.as_view(), name='view'),
    path('<int:contact_id>/edit/', ContactUpdate.as_view(), name='edit'),
]
