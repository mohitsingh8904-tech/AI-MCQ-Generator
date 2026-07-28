from django.db import models
from django.contrib.auth.models import User


class UploadedNotes(models.Model):
    file = models.FileField(upload_to="notes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notes {self.id} - {self.file.name}"


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total}"
