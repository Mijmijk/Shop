from django.contrib import admin
from django.urls import path
from shop.views import catalog, orders, create_order
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
	path('catalog/', catalog, name='catalog'),
	path('orders/', orders, name= 'orders'),
	path('create_order/', create_order, name= 'cr_order'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)