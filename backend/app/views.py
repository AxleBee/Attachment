from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.utils.http import is_safe_url
from django.urls import reverse
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
            return redirect('login')
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
                return redirect('supervisor_dashboard')
            if user.user_type == "employer":
                return redirect('employer_dashboard')
            if user.user_type == "student":
                return redirect('add_attachment')
            
            messages.success(request, 'Logged In successfully.')

        else:
            messages.warning(request, 'password or email is incorrect.')
    return render(request, 'app/login.html', context={"email": email})


def logout_view(request):
    print(request.user.user_type)
    messages.success(request, 'Logged out In successfully.')
    logout(request)
    return redirect('login')


# # Student Views ##
@login_required(login_url='/attachment/login/')
def add_attachment(request):
    current_user = request.user
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
            student=request.user.student

        )
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
        level = int(request.POST.get('year'))
        pic = request.FILES.get('pic')

        if not current_user.updated_profile:
            profile = Student.objects.create(

                admission_no=admission_no,
                name=name,
                course=course,
                year=level,
                photo_url=pic,
                user=current_user

            )
            profile.user.updated_profile = True
            current_user.save()
        else:
            student = Student.objects.get(
                admission_no=current_user.student.admission_no)
            student.admission_no = admission_no
            student.name = name
            student.course = course
            student.year = level
            student.photo_url = pic
            student.save()
    return render(request, 'app/student_profile.html', locals())


@login_required(login_url='/attachment/login/')
def add_logbook(request):
    current_user = request.user
    if request.method == 'POST':
        activity = request.POST.get('activity')
        date = request.POST.get('date')

        log_book = LogBook.objects.create(

            activity=activity,
            date=date,
            student=request.user.student
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
        log_books = LogBook.objects.filter(date__range=(
            from_date, to_date), student=current_user.student)
        return render(request, "app/view-logbooks.html", locals())
    return render(request, "app/view-logbooks.html", locals())


def view_comments(request):
    pass

# Supervisor views


def supervisor_dashboard(request):
    supervisor = request.user.supervisor
    if not request.user.updated_profile:
        messages.success(
            request, f'update your profile detail')
        return redirect('supervisor_profile')
    students = User.objects.filter(user_type='student')[::-1]
    return render(request, "app/supervisor-dashboard.html", locals())


@login_required(login_url='/attachment/login/')
def supervisor_profile(request):
    current_user = request.user
    profile = Supervisor.objects.filter(user=current_user)

    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        phone = request.POST.get("phone")
        pic = request.FILES.get('pic')

        if not current_user.updated_profile:
            profile = Supervisor.objects.create(

                name=name,
                postion=position,
                phone=phone,
                photo_url=pic,
                user=current_user

            )
            profile.user.updated_profile = True
            current_user.save()
        else:
            supervisor = Supervisor.objects.get(
                pk=current_user.pk)

            supervisor.name = name
            supervisor.postion = position
            supervisor.phone = phone
            supervisor.photo_url = pic
            supervisor.save()
    return render(request, 'app/supervisor_profile.html', locals())


def supervisor_feedback(request, email):
    student = User.objects.get(email=email).student
    log_books = None
    if request.method == 'POST':
        from_date = request.POST.get('from')
        to_date = request.POST.get('to')
        print(f'from {from_date} , end {to_date} {student}')
        log_books = LogBook.objects.filter(
            date__range=(from_date, to_date), student=student)
    return render(request, "app/logbook_feedback.html", locals())


def logbook_comment(request, log_id):
    supervisor = request.user.supervisor
    logbook = get_object_or_404(LogBook, pk=log_id)
    if request.method == 'POST':
        comment = Comments.objects.create(

            comment=request.POST.get('comment'),
            logbook=logbook,
            supervisor=supervisor
        )
        logbook.status = True
        logbook.save()
        next_url = request.POST.get('next')
        # if not next_url or not is_safe_url(url=next_url, allowed_hosts=request.get_host()):
        #     next_url = reverse('supervisor_dashboard')
        return HttpResponseRedirect(next_url)


def employer_dashboard(request):
    current_user = request.user
    if not request.user.updated_profile:
        messages.success(
            request, f'update your profile detail')
        return redirect('employer_profile')
    students = User.objects.filter(user_type='student')[::-1]

    return render(request, "app/employer_dashboard.html", locals())


@login_required(login_url='/attachment/login/')
def employer_profile(request):
    current_user = request.user
    profile = Employer.objects.filter(user=current_user)

    if request.method == 'POST':
        name = request.POST.get('name')
        organisation = request.POST.get('organisation')
        position = request.POST.get('position')
        phone = request.POST.get("phone")
        pic = request.FILES.get('pic')

        if not current_user.updated_profile:
            profile = Employer.objects.create(

                name=name,
                postion=position,
                organisation=organisation,
                phone=phone,
                photo_url=pic,
                user=current_user

            )
            profile.user.updated_profile = True
            current_user.save()
        else:
            employer = Employer.objects.get(
                pk=current_user.pk)

            employer.name = name
            employer.organisation=organisation
            employer.postion = position
            employer.phone = phone
            employer.photo_url = pic
            employer.save()
    return render(request, 'app/employer_profile.html', locals())


def employer_comment(request, email):
    current_user = request.user
    student = User.objects.get(email=email).student
    if request.method == 'POST':
        comment = EmployerComment.objects.create(

            comment=request.POST.get('feedback'),
            student = student
        )
        return redirect('employer_dashboard')
    return render(request, "app/employer_comment.html", locals())
