from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Record(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    user = models.ForeignKey(User, models.CASCADE)
    remark = models.TextField(default="",blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)

    def __str__(self) -> str:
        return self.title.title()
