import math

from django.contrib.auth.models import User
from django.db import models

from app.media_management.constants import ALLOWED_MEDIA_TYPES


class MediaItem(models.Model):
    """
    Object intended to capture and Image pre- and post-processing storage .
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    original_media_url = models.URLField(max_length=200)

    clear_cut_media_url = models.URLField(max_length=200)

    media_type = models.models.IntegerField(choices=ALLOWED_MEDIA_TYPES, default=0)
