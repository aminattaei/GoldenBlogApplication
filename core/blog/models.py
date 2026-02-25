from django.db import models

class Post(models.Model):
    authur = models.ForeignKey('User',on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    published = models.BooleanField(default=False)

    published_date = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
