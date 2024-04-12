
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    full_name = forms.CharField(label='Full Name')  # Burada full_name alanını ekledik.

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "full_name"]

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    

    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    # Diğer alanlar
    published = models.BooleanField(default=False)
 

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)


class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    
    


    






    

    



    
