from django.db import models

class BlogPost(models.Model):
   title = models.CharField(max_length=100) 
   author = models.CharField(max_length=50, blank=True,)
   body = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)


   class Meta:
      ordering = ['-date_created']
   def __str__(self):
     return self.title 
   
     
   