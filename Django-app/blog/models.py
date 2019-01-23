from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)


    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
  return self.user.username


class DataFile(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(DataFile, self).save(*args, **kwargs)
        filename = self.data.url
        # Do anything you'd like with the data in filename
