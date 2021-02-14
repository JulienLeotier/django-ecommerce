from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("commerce.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
