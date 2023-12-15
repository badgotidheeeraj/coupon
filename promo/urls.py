from django.conf.urls.static import static
from django.urls import path, include
# from django.contrib import admin
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
        path('profile/', views.profile, name='dashboard'),   
        path('create/', views.create_post, name='create_post'),   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

