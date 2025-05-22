from django.db import models
from django.conf import settings

class LikeDislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10)
    content_id = models.PositiveIntegerField()
    vote = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'content_id')
