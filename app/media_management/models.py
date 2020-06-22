from django.contrib.auth.models import User
from django.db import models

from media_management import constants

from clear_cut.models import ClearCutConfig


class MediaItem(models.Model):
    """
    Object intended to capture and Image pre- and post-processing storage .
    """
    clear_cut_images = models.ManyToManyField('self', symmetrical=False)

    clear_cut_config = models.ForeignKey(ClearCutConfig, on_delete=models.CASCADE, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    media_type = models.IntegerField(choices=constants.ALLOWED_MEDIA_TYPES, default=0)

    description = models.TextField(max_length=1048, null=True)

    label = models.TextField(max_length=128, null=True)


class MediaImage(models.Model):
    """
    Data of a single processed image
    """
    media_item = models.ForeignKey(MediaItem, on_delete=models.CASCADE, null=False, related_name='clear_cut_image')

    media_url_original = models.URLField(max_length=200)

    media_url_clear_cut = models.URLField(max_length=200)
