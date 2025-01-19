from django.db import models
from users.models import User
from tag.models import Tag
import uuid

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(null=False, blank=False)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="comments", blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField('self', symmetrical=False, related_name="replied_to", blank=True)

    def __str__(self):
        # Truncate text to avoid displaying excessively long comments
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
    