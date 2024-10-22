from django.contrib import admin

from .models import Books, Course, Issue_book, Student

# Register your models here.
admin.site.register(Books)
admin.site.register(Course)
admin.site.register(Issue_book)
admin.site.register(Student)
