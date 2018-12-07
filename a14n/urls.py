from django.urls import include, path

from a14n import views as a14n_views

urlpatterns = [
    path('signup/', a14n_views.signup, name='a14n-signup'),
    # path('', include('django.contrib.auth.urls')),
]
