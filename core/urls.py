# from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView as tw

from core import views as core_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', tw.as_view(template_name='home.html'), name='home'),
    path('about/', tw.as_view(template_name="about.html"), name='about'),
    path('hopla', core_views.hopla, name='hopla'),
    path('my/', include('a14n.urls')),
    path('user/', include('user.urls')),
    path('lead/', include('lead.urls')),
]
