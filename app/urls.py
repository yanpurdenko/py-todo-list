from django.conf.urls.static import static
from django.urls import path

from todo import settings
from app.views import (
    index,
)

urlpatterns = [
    path("", index, name=index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


app_name = "app"
