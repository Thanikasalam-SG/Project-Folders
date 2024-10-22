from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_fun, name='log'),
    path('register', views.reg_fun, name='register'),

    path('home', views.home_fun, name='home'),

    path('addbook', views.addbook_fun, name='addbook'),
    path('displaybook', views.displaybook_fun, name='displaybook'),
    path('update/<int:id>', views.update_book_fun, name='up'),
    path('delete/<int:id>', views.delete_book_fun, name='del'),

    path('getstudent', views.get_Student_fun, name='getstudent'),
    path('assignbook', views.assignbook_fun, name='assignbook'),

    path('displayassign', views.display_assign_fun, name='displayassign'),
    path('del_issue/<int:id>', views.delete_issue_fun, name='del_issue'),
    path('updt_issue/<int:id>', views.updt_issue_fun, name='updt_issue'),


    # Student page urls
    path('addstud', views.add_stud_fun, name='addstud'),
    path('studhome', views.stud_home_fun, name='studhome'),
    path('stud_books', views.stud_book_fun, name='stud_books'),
    path('getprofile', views.get_prof_fun, name='getprof'),
    path('updtprof/<int:id>', views.update_prof_fun, name='updtprof'),

    path('log_out', views.log_out_fun, name='log_out'),
]
