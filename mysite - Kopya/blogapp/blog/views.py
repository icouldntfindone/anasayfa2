from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from .forms import RegisterForm
from .forms import BlogForm
from .models import Blog
from .models import Forum
from django.contrib.auth.models import User # type: ignore
from .models import UserProfile
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm




def user_logout(request):
    logout(request)
    return redirect('main3')



    

def main(request):
    return render(request,'blog/main.html')

def main2(request):
    return render(request,'blog/main2.html')

def main3(request):
    return render(request,'blog/main3.html')

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('details',)  # Burada 'blog_detail' url ismi ile blogun detay sayfasına yönlendirme yapılacak.
    else:
        form = BlogForm()
    return render(request, 'blog/blog_create.html', {'form': form})

def details(request):
    # Yayımlanan blogları al
    published_blogs =  published_blogs = Blog.objects.all()
    return render(request, 'blog/details.html', {'published_blogs': published_blogs})

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'blog/forum_list.html', {'forums': forums})

def forum_detail(request):
    forums = Forum.objects.all()
    return render(request, 'blog/forum_detail.html', {'forums': forums})






def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main2')
            else:
                # Giriş başarısız olduğunda bir hata mesajı gösterebilirsiniz.
                pass  # Burada hata mesajı gösterme işlemi yapılabilir.
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


from django.views import View

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'blog/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'"{username}" adlı kullanıcı için hesap oluşturuldu.')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})







# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super().form_valid(form)



class ResetPasswordView(PasswordResetView):
    template_name = 'blog/password_reset.html'
    email_template_name = 'blog/password_reset_email.html'
    subject_template_name = 'blog/password_reset_complete.html'  # Şablon dosyanızın yolunu doğru şekilde belirtin
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('anasayfa')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'blog/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('anasayfa')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'user_form': user_form, 'profile_form': profile_form})




