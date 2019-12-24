from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from product.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),

    #path('product/', include('product.urls')),
    path('user/', include('user.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # сервер разработки Django будет
    # отвечать за службу мультимедийных файлов во время разработки.
