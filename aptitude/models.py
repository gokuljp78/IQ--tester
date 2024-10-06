from django.db import models

# Create your models here.

class question(models.Model):
    quest = models.TextField()
    cho1  = models.TextField()
    cho2  = models.TextField()
    cho3  = models.TextField()
    cho4  = models.TextField()
    ans  = models.TextField()
    exp = models.TextField(null=True,blank=True)

class profile(models.Model):
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    profile_img = models.ImageField(null=True,blank=True,upload_to="pics/")
    attempts = models.IntegerField(null=True,blank=True)
    scores = models.TextField(null=True,blank=True)
