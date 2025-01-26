from django.db import models

# Create your models here.

# Category model
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)                 # max length of 128 characters for name field in Category model  
    views = models.IntegerField(default=0)                               # default value is 0
    likes = models.IntegerField(default=0)                               # default value is 0

    class Meta:                                                          # Meta class for Category model
        verbose_name_plural = 'Categories'                               # verbose name for Category model

    def __str__(self):                                                   # string representation of Category model
        return self.name                                                 # return name of Category model
    

# Page model
class Page(models.Model):   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)     # foreign key to Category model with CASCADE delete
    title = models.CharField(max_length=128)                             # max length of 128 characters for title field in Page model 
    url = models.URLField()                                              # URL field for url field in Page model 
    views = models.IntegerField(default=0)                               # default value is 0

    def __str__(self):                                                   # string representation of Page model
        return self.title                                                # return title of Page model