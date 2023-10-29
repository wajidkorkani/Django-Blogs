from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='media', null=True, blank=True)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    categoery = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='save')
    
    def geturl(self):
        return reverse("about", args=[self.slug])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"