from django.contrib import admin
from django.urls import path
from shop.views import catalog, orders, create_order, product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
	path('catalog/', catalog, name='catalog'),
	path('orders/', orders, name= 'orders'),
	path('create_order/<int:id>/', create_order, name= 'cr_order'),
	path('product/<int:id>/', product_detail, name= 'product_detail')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)