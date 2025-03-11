from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField(unique=True)
    short_hash = models.URLField(max_length=10, unique=True)

    def get_short_url(self):
        return f"http://127.0.0.1:8000/api/{self.short_hash}/"