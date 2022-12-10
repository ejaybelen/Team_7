from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Model
from django.contrib.auth.models import User


# Tables

class Instructor(models.Model):
    abbrev = models.CharField(max_length=50)
    fname = models.ForeignKey(User, blank=True, related_name='fname', on_delete=models.CASCADE)
    lname = models.ForeignKey(User, blank=True, related_name='lname', on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.abbrev + ' ' + self.fname + ' ' + self.lname

class Signature(models.Model):
    prep = models.ForeignKey(User, blank=True, related_name='prep', on_delete=models.CASCADE)
    note1 = models.ForeignKey(User, blank=True, related_name='note1', on_delete=models.CASCADE)
    note2 = models.ForeignKey(User, blank=True, related_name='note2', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.prep

class Course(models.Model):
    c_code = models.CharField('Course Code', max_length=20)
    name = models.CharField('Course Name', max_length=50)
    credits = models.PositiveIntegerField('Credit Units')
    contact_hours = models.PositiveIntegerField('Contact Hours')
    instructor = models.ManyToManyField(Instructor, blank=True)
    textbook = models.CharField('Textbooks', max_length=100)
    textbook2 = models.CharField('Other Supplemental Materials', max_length=100, null=True)
    course_description = models.TextField()
    prereq = models.CharField('Prerequisites', max_length=100)
    co_req = models.CharField('Co-requisites', max_length=100)
    course_classification = models.CharField('Course Classification', max_length=50)
    course_objective = models.TextField()
    ILO = RichTextField(blank=True, null=True)
    s_outcomes = RichTextField(blank=True, null=True)
    prelim = RichTextField(blank=True, null=True)
    midterm = RichTextField(blank=True, null=True)
    finals = RichTextField(blank=True, null=True)
    signatories = models.ForeignKey(Signature, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.c_code + ' ' + self.name

