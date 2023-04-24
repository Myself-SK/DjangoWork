from django.urls import path
from django.conf import settings

from .views import PostView
from django.conf.urls.static import static

urlpatterns = [
    path('', PostView.as_view(), name="post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
