# from django.contrib import admin
from django.urls import include, path

from core import views as core_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('about', core_views.about, name='about'),
    path('hopla', core_views.hopla, name='hopla'),
    path('my/', include('a14n.urls')),
    path('user/', include('user.urls')),
    path('lead/', include('lead.urls')),
]
