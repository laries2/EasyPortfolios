from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100)
    skill3 = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='uploads/profile/')
    background_img = models.ImageField(upload_to='uploads/background/')
    profession = models.CharField(max_length=100)
    overview = models.TextField()
    contact_number = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    portfolio = models.CharField(max_length=100,unique=True)
    role1 = models.CharField(max_length=100)
    role1_info = models.TextField()
    role2 = models.CharField(max_length=100)
    role2_info = models.TextField()
    role3 = models.CharField(max_length=100)
    role3_info = models.TextField()

    def __str__(self):
        return self.portfolio

    # image = models.ImageField()
    # description = models.TextField()
    # likes = models.IntegerField(default= 0)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
