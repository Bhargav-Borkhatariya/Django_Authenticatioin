from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(User):
    """
    Here in this model we import the auth.user model and add image field.
    and we gave upload direction to the media/images directory.
    """

    image = models.ImageField(upload_to="images/", blank=True)
