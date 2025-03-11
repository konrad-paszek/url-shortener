from django.urls import path
from .api_views import CreateShortUrl, RedirectToOriginal

urlpatterns = [
    path("url-shortener/", CreateShortUrl.as_view(), name='api-shortener'),
    path('<str:short_hash>/', RedirectToOriginal.as_view(), name='redirect-url'),
]