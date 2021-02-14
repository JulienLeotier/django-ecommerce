from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from commerce.views import index, sign_in, sign_out, shipping, display_cart, display_category, display_product, add_address, add_to_cart, account, addresses, checkout, clear_cart, confirmation, orders

urlpatterns = [
    url(r'^$', index),
    url(r'^sign-in/(?P<goto>\w+:\w+)/$', sign_in),
    url(r'^sign-in/$', sign_in),
    url(r'^sign-out/$', sign_out),
    url(r'^product/(?P<product_id>\d+)/$', display_product),
    url(r'^category/(?P<category_id>\d+)$', display_category),
    url(r'^add-to-cart/(?P<product_id>\d+)/(?P<qty>\d+)/$', add_to_cart),
    url(r'^clear-cart/$', clear_cart),
    url(r'^cart/$', display_cart),
    url(r'^shipping/$', shipping),
    url(r'^add-address/$', add_address),
    url(r'^checkout/$', checkout),
    url(r'^confirmation/$', confirmation),
    url(r'^account/$', account),
    url(r'^orders/$', orders),
    url(r'^addresses/$', addresses),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
