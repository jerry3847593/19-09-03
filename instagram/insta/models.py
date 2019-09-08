from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.ImageField()
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def like_count(self):
        return self.like_set.count()

    class Meta:
        ordering=['-updated']

    def _str_(self):
        return '%s  - %s' % (self.id, self.user)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# Create your models here.
