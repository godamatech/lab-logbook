from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Record(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=True, default=None)

    def __str__(self) -> str:
        return self.title.title()
