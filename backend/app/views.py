from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
            if user.user_type == "supervisor":
                pass
            if user.user_type == "employer":
                pass
            if user.user_type == "student":
                return redirect('add_attachment')

        else:
            messages.warning(request, 'password or email is incorrect.')
    return render(request, 'app/login.html', context={"email": email})


def logout_view(request):
    print(request.user.user_type)
    logout(request)
    return redirect('login')


# # Student Views ##
@login_required(login_url='/attachment/login/')
def add_attachment(request):
    # date1 = request.user.last_login
    # date2 = request.user.date_joined
    # if (date1.year, date1.day == date2.year, date2.day):
    if not request.user.updated_profile:
        messages.success(
            request, f'update your profile detail')
        return redirect('student_profile')

    if request.method == 'POST':
        attachment_name = request.POST.get('attachment')
        department_name = request.POST.get('department')
        start_date = request.POST.get("start")
        end_date = request.POST.get('end')
        attachment = Attachment.objects.create(

            attachment_name=attachment_name,
            department_name=department_name,
            start_date=start_date,
            end_date=end_date,
            student = request.user.student

        )
        # attachment.student = request.user.student
        attachment.save()

    return render(request, 'app/attachment.html', locals())

@login_required(login_url='/attachment/login/')
def view_attachments(request):
    attachments = Attachment.objects.all()[::-1]
    return render(request, "app/view-attachment.html", locals())

@login_required(login_url='/attachment/login/')
def student_profile(request):
    current_user = request.user
    profile = Student.objects.filter(user=current_user)

    if request.method == 'POST':
        name = request.POST.get('name')
        admission_no = request.POST.get('admission_no')
        course = request.POST.get("course")
        print(type(request.POST.get('year')))
        year = int(request.POST.get('year'))
        pic = request.FILES.get('pic')
        print(pic, end="$$$$$$$$$$$$$$$$")
        profile = Student.objects.create(
            
            admission_no=admission_no,
            name=name,
            course=course,
            year=year,
            photo_url=pic,
            user = current_user

        )
    
        # profile.user = current_user
        profile.user.updated_profile = True
        current_user.save()
        
        
    return render(request, 'app/student_profile.html', locals())

@login_required(login_url='/attachment/login/')
def add_logbook(request):
    
    if request.method == 'POST':
        activity = request.POST.get('activity')
        date = request.POST.get('date')
    
        log_book = LogBook.objects.create(
            
            activity = activity,
            date = date,
            student = request.user.student
        )

    return render(request, 'app/add-logbook.html', locals())
        

@login_required(login_url='/attachment/login/')
def search_logbook(request):
    current_user = request.user
    print(current_user.student.photo_url.url)
    log_books = None
    if request.method == 'POST':
        from_date = request.POST.get('from')
        to_date = request.POST.get('to')
        log_books = LogBook.objects.filter(date__range=(from_date, to_date))
        return render(request, "app/view-logbooks.html", locals())
    return render(request, "app/view-logbooks.html", locals())        

def view_comments(request):
    pass

#Supervisor Commednts

def supervisor_dashboard():
    pass

def supervisor_feedback():
    pass

def supervisor_profile():
    pass