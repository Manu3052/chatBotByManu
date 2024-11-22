from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework import routers

from chat import views
from chat.views import ChannelViewSet
from message.views import MessageViewSet

router = routers.DefaultRouter()
router.register("channel", ChannelViewSet, basename="channel")
router.register("message", MessageViewSet, basename="message")
# router.register("support-agent", SupportAgentViewSet, basename="support-agent")
# router.register("contact", ContactViewSet, basename="contact")


urlpatterns = [
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
