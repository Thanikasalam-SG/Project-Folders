from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50,default=None)

    def __str__(self):
        return f'{self.course_name}'


class Books(models.Model):
    book_name = models.CharField(max_length=50,default=None)
    author_name = models.CharField(max_length=50,default=None)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book_name}'


class Student(models.Model):
    stud_name = models.CharField(max_length=50,default=None)
    stud_password = models.CharField(max_length=50,default='1234')  # or we can use null also
    stud_phno = models.BigIntegerField(default=None)
    stud_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    stud_semester = models.IntegerField(default=None)
    stud_image = models.ImageField(default=None, upload_to='stud_profile')

    def __str__(self):
        return f'{self.stud_name}'


class Issue_book(models.Model):
    stud_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    book_name = models.ForeignKey(Books,on_delete=models.CASCADE)
    start_date = models.DateField(default=None)
    end_date = models.DateField(default=None)