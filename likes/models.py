from django.db import models
from accounts.models import User
from serials.models import Product

class PostLikes(models.Model):
    users_like=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users_like')
    posts_like = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='posts_like')
