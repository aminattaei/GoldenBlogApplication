from django.db import models


class Post(models.Model):
    """
    This is the model for the blog post. It has a foreign key to the User model, which is the author of the post. It also has a foreign key to the Category model, which is the category of the post. The published field is a boolean field that indicates whether the post is published or not. The published_date field is a datetime field that indicates when the post was published. The created_time field is a datetime field that indicates when the post was created. The updated_time field is a datetime field that indicates when the post was last updated.
    """
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
