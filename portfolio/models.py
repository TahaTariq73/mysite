from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    post_id = models.AutoField(auto_created=True, primary_key=True)
    post_title = models.CharField(max_length=1000, default="")
    post_content = models.TextField(max_length=5000, default="")
    post_img = models.ImageField(upload_to="Images", default="")
    post_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.post_id}: {self.post_title}"

class Comment(models.Model):
    comment_id = models.AutoField(auto_created=True, primary_key=True)
    comment_content = models.TextField(max_length=5000, default="", null=True)
    comment_user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    comment_parent = models.ForeignKey("self", blank=True, on_delete=models.CASCADE, null=True)
    comment_post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE, null=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.comment_user.username}"