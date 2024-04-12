from django.contrib import admin
from .models import Blog
from .models import Forum
from .models import Thread
from .models import UserProfile
from .models import Profile
from django.contrib.auth.models import User


for user in User.objects.all():
    Profile.objects.get_or_create(user=user)

admin.site.register(Profile)


admin.site.register(Blog)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(UserProfile)






