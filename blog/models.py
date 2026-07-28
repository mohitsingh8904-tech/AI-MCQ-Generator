from django.db import models  

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    tag = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

