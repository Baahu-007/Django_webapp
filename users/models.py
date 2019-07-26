from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#models.Model signifies inheritence property
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
        #OneToOneField means
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
