from django.db import models
from django.utils import timezone
<<<<<<< HEAD
from django.db.models.functions import Now
from django.conf import settings
from django.urls  import reverse


class PublishedManager(models.Manager):
    def get_queryset(slef):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


=======
from django.conf import settings
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", 'Draft'
        PUBLISHED = 'PB', 'Published'
<<<<<<< HEAD

    
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
=======
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='publish')
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)


=======
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
<<<<<<< HEAD
    
=======

>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df


    def __str__(self):
        return self.title

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse('blog:post_detail',
        args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
            ]  
        )
=======

    def get_absolute_url(self):
        return reverse('blog:post_detail',  args=[self.publish.year,
                                                  self.publish.month,
                                                  self.publish.day,
                                                  self.slug])
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    updated = models.DateTimeField(auto_now=True)
=======
    updated=models.DateTimeField(auto_now=True)
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
<<<<<<< HEAD
            models.Index(fields=['created'])
        ]


    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

        
=======
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
