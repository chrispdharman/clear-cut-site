from django.db import models


class ClearCutConfig(models.Model):
    """
    Object to store ClearCut parameters.
    """
    is_default = models.BooleanField(default=False)

    hyperparameter_one = models.IntegerField()
