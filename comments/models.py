from django.db import models
from accounts.models import User

from serials.models import Product

class Comment(models.Model):
    films = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    like =models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    
    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.films}'

    def children(self):
        return Comment.objects.filter(parent=self)

@property
def is_parent(self):
    if self.parent is not None:
        return False
    return True
