from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']  # Order tags alphabetically
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
