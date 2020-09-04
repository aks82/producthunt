from django.db import models
from django.contrib.auth.models import User

#product class
class Product(models.Model):
    # title
    title = models.CharField(max_length=255)
    # url
    url = models.TextField()
    # pubdate
    pub_date = models.DateTimeField()
    # votes
    vote_count = models.IntegerField(default=1)
    # image
    image = models.ImageField(upload_to='catalog/images/')
    # icon
    icon = models.ImageField(upload_to='catalog/images/')
    # body
    body = models.TextField()
    #hunter
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title






