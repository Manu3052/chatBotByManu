from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

from chat import views
from chat.views import ChannelViewSet
from message.views import MessageViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Chatbot Api",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register("channel", ChannelViewSet, basename="channel")
router.register("message", MessageViewSet, basename="message")
# router.register("support-agent", SupportAgentViewSet, basename="support-agent")
# router.register("contact", ContactViewSet, basename="contact")


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
