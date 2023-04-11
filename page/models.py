from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=10)
    description=models.CharField(max_length=600)
    auther=models.CharField(max_length=10)
    published_date=models.DateField(auto_now=False)

    