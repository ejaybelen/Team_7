from django import forms
from django.forms import ModelForm
from .models import Course, Instructor

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            'c_code': 'Course Code',
            'name': 'Course Name',
            'credits': 'Credits',
            'contact_hours': 'Contact Hours',
            'instructor': 'Instructor',
            'textbook': 'Textbook',
            'textbook2':'Other Supplemental Materials',
            'course_description': 'Course Description',
            'prereq': 'Prerequisites',
            'co_req': 'Co-requisites',
            'course_classification': 'Course Classification (Required/elective/selected elective',
            'course_objective': 'Course Objective',
            'ILO': 'Course Outcomes',
            's_outcomes': 'Student Outcomes Addressed by the Course',
            'prelim': 'Prelim Period',
            'midterm': 'Midterm Period',
            'finals': 'Final Period',
        }
        
        widgets = {
            'c_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Credits'}),
            'contact_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contact Hours'}),
            'instructor': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Instructor'}),
            'textbook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Textbook'}),
            'textbook2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Textbook'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Description'}),
            'prereq': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prerequisites'}),
            'co_req': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Co-requisites'}),
            'course_classification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(Required/elective/selected elective)'}),
            'course_objective': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Objective'}),
            'ILO': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Outcomes'}),
            's_outcomes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Student Outcomes'}),
            'prelim': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Prelim Period'}),
            'midterm': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Midterm Period'}),
            'finals': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Final Period'}),
        }

