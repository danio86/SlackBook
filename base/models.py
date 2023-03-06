from django.db import models
from django.contrib.auth.models import User
# django has a buildin default User(model) with first name, last name,...
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Channel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(
    #      User, on_delete=models.CASCADE, related_name="blog_posts"
    # )
    # featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # likes = models.ManyToManyField(
    #     User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    # def number_of_likes(self):
    #     return self.likes.count()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    # this says to which channel the post belongs
    # all posts are children of the Channel Class/Model.
    # If Channel or User gets deleted, all posts have to get deleted too.
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.body[0:30]
