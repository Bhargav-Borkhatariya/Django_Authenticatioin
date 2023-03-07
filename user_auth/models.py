from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(User):
    """
    Here in this model we import the auth.user model and add image field.
    and we gave upload direction to the media/images directory.
    """

    image = models.ImageField(upload_to="images/", blank=True)


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255, null=True)
    book_author = models.CharField(max_length=255, null=True)
    book_price = models.CharField(max_length=255, null=True)
    book_image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.book_name
