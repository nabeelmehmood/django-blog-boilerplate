from django.db import models
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=True)

    def user_directory_path(instance, filename): 
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
        return 'user_{0}/{1}'.format(instance.author.id, filename) 

    title_image = models.ImageField(upload_to=user_directory_path, default='default/default-image.jpeg', blank=True)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    
    post = models.ForeignKey('blog.Post', related_name='comments', null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
    
    def __str__(self):
        return self.text


class Category(models.Model):

    title = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("post_list")
    
    def __str__(self):
        return self.title