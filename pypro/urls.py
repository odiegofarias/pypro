from django.contrib import admin
from django.urls import path, include
from base import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
