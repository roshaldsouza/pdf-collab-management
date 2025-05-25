from django.db import models
from django.contrib.auth.models import User
import uuid
class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shareable_link = models.CharField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.shareable_link:  # Generate only if empty
            self.shareable_link = uuid.uuid4().hex[:20]
        super().save(*args, **kwargs)


class Comment(models.Model):
    document = models.ForeignKey(PDFDocument, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest_name = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)