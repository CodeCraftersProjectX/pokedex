from django.contrib import admin
from . import views
from django.urls import include, path

app_name = 'pokedex'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('v1/', include('api_v1.urls')),
]
