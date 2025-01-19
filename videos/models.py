from django.db import models
from comments.models import Comment
from tag.models import Tag
import uuid

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(null=False, blank=False)
    thumb_nail = models.ImageField(upload_to='thumb_nail/', blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    posted_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.ManyToManyField(Comment, related_name="videos", blank=True)
    tags = models.ManyToManyField(Tag, related_name="videos", blank=True)
    content = models.FileField(upload_to='videos/', blank=False, null=False)
    valid_view = models.PositiveIntegerField(default=0)
    video_watch_percentage = models.DecimalField(default=0)

    def __str__(self):
        return self.title