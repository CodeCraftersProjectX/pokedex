from django.contrib import admin
from django.urls import include, path
from django.urls.resolvers import URLPattern, URLResolver


urlpatterns: list[URLPattern | URLResolver] = [
    # path('v1/', include('api_v1.urls')),
    # path('master/', include('apps.master.urls')),
    # path('', include('apps.coordinate.urls')),
    # path('', include('apps.instagram.urls')),
    path('', include('pokedex.urls')),
    path('admin/', admin.site.urls),
]
