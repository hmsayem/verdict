from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        # Add New Post
        # return reverse('detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=250, default='Miscellaneous')

    likes = models.ManyToManyField(User, related_name='post_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title) + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + " | " + str(self.user.username)
