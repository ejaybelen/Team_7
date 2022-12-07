from django.db import models

# Tables

class Instructor(models.Model):
    abbrev = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.abbrev + ' ' + self.fname + ' ' + self.lname

class Signature(models.Model):
    prep = models.CharField(max_length=100)
    note1 = models.CharField(max_length=100)
    note2 = models.CharField(max_length=100)
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
    ILO = models.TextField()
    s_outcomes = models.TextField()
    prelim = models.TextField()
    midterm = models.TextField()
    finals = models.TextField()
    signatories = models.ForeignKey(Signature, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.c_code + ' ' + self.name

