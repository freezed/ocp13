from django.urls import path
from organact import views as organact_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', organact_views.home, name='home'),
    path('about', organact_views.about, name='about'),
]
