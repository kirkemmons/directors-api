from django.db import models
from ..models.director import Director
from django.contrib.auth import get_user_model

class Film(models.Model):
    title = models.CharField(max_length=256)
    release = models.IntegerField(null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    image = models.CharField(max_length=256)
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name='films', blank=True, null=True)

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def as_dict(self):
        """Returns dictionary version of Film models"""
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release,
            'description': self.description,
            'image': self.image,
            'director': self.director,

        }
