from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import *

# # Authentication Views ##


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{form.cleaned_data["email"]} registered successfullly')
    context = {'form': form}
    return render(request, 'app/register.html', context)


def login_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        if current_user.user_type == "supervisor":
            pass
        if current_user.user_type == "employer":
            pass
        if current_user.user_type == "student":
            return redirect('add_attachment')
    email = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, f'{user.username} logged in successfully.')

        else:
            messages.warning(request, 'password or email is incorrect.')
    return render(request, 'app/login.html', context={"email": email})


def logout_view(request):
    print(request.user)
    logout(request)
    return redirect('login')


# # Student Views ##
def add_attachment(request):
    if (request.user.last_login == request.user.date_joined):
        messages.success(
            request, f'update your profile detail')
        return redirect('student_profile')

    if request.method == 'POST':
        attachment_name = request.POST.get('attachment')
        organisation_name = request.POST.get('organisation')
        start_date = request.POST.get("start")
        end_date = request.POST.get('end')
        attachment = Attachment.objects.create(

            attachment_name=attachment_name,
            organisation_name=organisation_name,
            start_date=start_date,
            end_date=end_date

        )
        attachment.student = request.user.student
        attachment.save()
    
    return (request, 'app/attachment.html', locals())


def add_profile(request):
    pass


def add_logbook(request):
    pass


def view_comments(request):
    pass
