
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from .views import profile,RegisterView
from django.contrib.auth import views as auth_views
from blog.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from blog.forms import LoginForm


urlpatterns = [
    path('', views.main, name='anasayfa'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('main3/', views.main3, name='main3'),
    path('main2/', views.main2, name='main2'),
    path('blog/', views.create_blog, name='create_blog'),
    path('details/', views.details, name='details'),
    path('forum_list/', views.forum_list, name='forum_list'),
    path('forum_detail/', views.forum_detail, name='forum_detail'),
    path('profile/', profile, name='profile'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)