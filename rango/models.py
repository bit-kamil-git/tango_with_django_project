from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

max = 128
# Category model
class Category(models.Model):                                             
    name = models.CharField(max_length=max, unique=True)                 # max length of 128 characters for name field in Category model  
    views = models.IntegerField(default=0)                               # default value is 0
    likes = models.IntegerField(default=0)                               # default value is 0
    slug = models.SlugField(unique=True)                                 # slug field for Category model

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:                                                          # Meta class for Category model
        verbose_name_plural = 'categories'                               # verbose name for Category model

    def __str__(self):                                                   # string representation of Category model
        return self.name                                                 # return name of Category model
    

# Page model
class Page(models.Model):   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)     # foreign key to Category model with CASCADE delete
    title = models.CharField(max_length = max)                             # max length of 128 characters for title field in Page model 
    url = models.URLField()                                              # URL field for url field in Page model 
    views = models.IntegerField(default=0)                               # default value is 0

    def __str__(self):                                                   # string representation of Page model
        return self.title                                                # return title of Page model
    

class  UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username