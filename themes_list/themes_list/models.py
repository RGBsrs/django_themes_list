from django.db import models
from django.urls import reverse

class Theme(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('theme', kwargs={'pk': self.id})
