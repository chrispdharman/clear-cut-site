from django.db import models


class ClearCutConfig(models.Model):
    """
    Object to store ClearCut parameters.
    """
    is_default = models.BooleanField(default=False)

    image_size_threshold = models.IntegerField(default=600)
    
    noisy_pixel_tolerance = models.IntegerField(default=4)
