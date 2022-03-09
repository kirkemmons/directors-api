from django.db import models
from django.contrib.auth import get_user_model

class Director(models.Model):
    name = models.CharField(max_length=256)
    roles = models.CharField(max_length=256)
    biography = models.CharField(max_length=512, blank=True, null=True)
    image = models.CharField(max_length=256)

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def as_dict(self):
        """Returns dictionary version of Director models"""
        return {
            'id': self.id,
            'name': self.name,
            'roles': self.roles,
            'biography': self.biography,
            'image': self.image,

        }
