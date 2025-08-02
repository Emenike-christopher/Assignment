from django.db import models

class BlogPost(models.Model):
   title = models.CharField(max_length=100) 
   author = models.CharField(max_length=50)
   body = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
     return self.title 