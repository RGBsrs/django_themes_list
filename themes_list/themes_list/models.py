from django.db import models

class Theme(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
