from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve
from rest_framework import routers
from channel import views

from channel.views import ChannelViewSet

router = routers.DefaultRouter()
router.register("channel", ChannelViewSet, basename="channel")


urlpatterns = [
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
