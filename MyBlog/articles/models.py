from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.SlugField()
    thumb=models.ImageField(blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
    @property
    def get_Cont(self):
        return self.content[0:50]


