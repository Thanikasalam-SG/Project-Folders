from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Books, Course, Issue_book, Student
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def login_fun(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        userPassword = request.POST['userPassword']
        user = authenticate(username=userName, password=userPassword)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                request.session['uid'] = request.POST['userName']
                return redirect('home')
            else:
                return render(request, 'login.html', {'data':'invalid credentials'})
        elif Student.objects.filter(Q(stud_name=userName) & Q(stud_password=userPassword)).exists():
            request.session['S_name'] = userName
            return render(request, 'student_template/stud_home.html', {'Name':request.session['S_name']})
        else:
            return render(request, 'login.html', {'data':'invalid credentials'})
    else:
        return render(request, 'login.html', {'data':''})


# ----------------------------------------------------------------------------------------------------------------------

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def reg_fun(request):
    if request.method == 'POST':
        username = request.POST['txtUserName']
        password = request.POST['txtPswd']
        email = request.POST['txtEmail']
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return render(request, 'register.html', {'data':'invalid credentials'})
        else:
            u1 = User.objects.create_superuser(username=username,password=password,email=email)
            u1.save()
            return render(request, 'login.html', {'data':''})
    else:
        return render(request,'register.html', {'data':''})


# ----------------------------------------------------------------------------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def add_stud_fun(request):
    c1 = Course.objects.all()
    if request.method == 'POST':
        s1 = Student()
        s1.stud_name = request.POST['txtName']
        s1.stud_course = Course.objects.get(course_name = request.POST['ddlCourse'])
        s1.stud_phno = request.POST['txtPhno']
        s1.stud_semester = request.POST['txtSem']
        s1.stud_password = request.POST['txtPswd']
        s1.stud_image = request.POST['Img']
        s1.save()
        return redirect('log')
    return render(request, 'student_template/add_student.html', {'course':c1})

# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def home_fun(request):
    return render(request, 'books_template/home.html')

# ----------------------------------------------------------------------------------------------------------------------


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def addbook_fun(request):
    if request.method == 'POST':
        c1 = Course.objects.all()
        b1 = Books()
        b1.book_name = request.POST['txtBookName']
        b1.author_name = request.POST['txtAuthorName']
        b1.course_name = Course.objects.get(course_name = request.POST['ddlCourseName'])
        b1.save()
        return render(request, 'books_template/add_book.html', {'course': c1, 'msg': 'added successfully'})
    else:
        c1 = Course.objects.all()
        return render(request, 'books_template/add_book.html', {'course':c1, 'msg': '', 'res': False})


# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def displaybook_fun(request):
    books = Books.objects.all()
    return render(request, 'books_template/display_book.html', {'books':books})

# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def update_book_fun(request,id):
    book = Books.objects.get(id=id)
    c1 = Course.objects.all()
    if request.method == 'POST':
        book.book_name = request.POST['txtBookName']
        book.author_name = request.POST['txtAuthorName']
        book.course_name = Course.objects.get(course_name=request.POST['ddlCourseName'])
        book.save()
        return redirect('displaybook')
    return render(request, 'books_template/update_book.html', {'books':book, 'course':c1})

# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revaidate=True, no_store=True)

@never_cache
def delete_book_fun(request,id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('displaybook')

# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def get_Student_fun(request):
    s1 = Student.objects.get(stud_phno=request.POST['txtPhno'])
    books = Books.objects.filter(course_name=s1.stud_course_id).all()
    return render(request, 'books_template/assign_book.html', {'Book':books, 'Stud':s1})

# ----------------------------------------------------------------------------------------------------------------------
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def assignbook_fun(request):
    books = Books.objects.all()
    if request.method == 'POST':
        i1 = Issue_book()
        i1.stud_name = Student.objects.get(stud_name=request.POST['txtName'])
        i1.book_name = Books.objects.get(book_name=request.POST['ddlBookName'])
        i1.start_date = request.POST['txtStartDate']
        i1.end_date = request.POST['txtEndDate']
        i1.save()
        return render(request, 'books_template/assign_book.html',
                      {'Book':books, 'Stud': '', 'msg':'assigned successfully', 'res':True})
    return render(request, 'books_template/assign_book.html', {'Book':books, 'Stud':'', 'msg':'', 'res':False})


# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def display_assign_fun(request):
    i1 = Issue_book.objects.all()
    return render(request, 'books_template/display_assign.html', {'issue':i1})


# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def delete_issue_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    i1.delete()
    return redirect('displayassign')


# ----------------------------------------------------------------------------------------------------------------------

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def updt_issue_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    s1 = Student.objects.get(id=i1.stud_name_id)
    books = Books.objects.filter(course_name=s1.stud_course)
    print(i1.start_date)
    if request.method == 'POST':
        i1.stud_name = Student.objects.get(stud_name=request.POST['txtName'])
        i1.book_name = Books.objects.get(book_name=request.POST['ddlBookName'])
        i1.start_date = request.POST['txtStartDate']
        i1.end_date = request.POST['txtEndDate']
        i1.save()
        return redirect('displayassign')
    return render(request, 'books_template/updt_issue.html',
                  {'Issue':i1, 'Stud':s1, 'Book':books})

# ----------------------------------------------------------------------------------------------------------------------


@cache_control(no_cache=True, must_revalidate=True, no_stora=True)
@never_cache
def stud_home_fun(request):
    return render(request, 'student_template/stud_home.html', {'Name':request.session['S_name']})

# ----------------------------------------------------------------------------------------------------------------------


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def stud_book_fun(request):
    s1 = Student.objects.get(stud_name=request.session['S_name'])
    i1 = Issue_book.objects.filter(stud_name=s1)
    return render(request, 'student_template/stud_books.html', {'data':i1})


# ----------------------------------------------------------------------------------------------------------------------

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def get_prof_fun(request):
    s1 = Student.objects.get(stud_name=request.session['S_name'])
    return render(request, 'student_template/stud_profile.html', {'data':s1})

# ----------------------------------------------------------------------------------------------------------------------

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def update_prof_fun(request,id):
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.stud_name = request.POST['txtName']
        s1.stud_phno = request.POST['txtPhno']
        s1.stud_semester = request.POST['txtSem']
        s1.stud_password = request.POST['txtPswd']
        s1.save()
        return redirect('getprof')
    return render(request, 'student_template/update_prof.html', {'data':s1})


# ----------------------------------------------------------------------------------------------------------------------

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')

