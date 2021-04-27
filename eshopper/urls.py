from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name = 'main'),
    path('', include('mainapp.urls')),
    path('blog/', include(('blogapp.urls', 'blogapp'), namespace='blog')),
    path('auth/', include(('authnapp.urls', 'authnapp'), namespace='auth')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)