from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ecommerce'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="accounts")),
    path('', include('store.urls', namespace="shop")),
    path('__debug__/', include('debug_toolbar.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)