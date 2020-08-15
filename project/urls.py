
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls' )),
    path('admin/', admin.site.urls),
    path('',include('document.urls')),
    path('home/',include('home.urls')),
    path('cabinet/',include('cabinet.urls')),
    path('document/',include('document.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

