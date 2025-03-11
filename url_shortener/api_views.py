from django.shortcuts import get_object_or_404, redirect
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortenedURL
from .serializers import UrlSerializer

class CreateShortUrl(CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = UrlSerializer

class RedirectToOriginal(APIView):
    def get(self, request, short_hash):
        obj = get_object_or_404(ShortenedURL, short_hash=short_hash)

        if request.GET.get('format') == 'json':
            return Response({"original_url": obj.original_url})

        return redirect(obj.original_url)