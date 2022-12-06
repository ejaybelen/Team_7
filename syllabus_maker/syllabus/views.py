from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Course
from .forms import CourseForm
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.db.models import Q

def add_syllabus(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_syllabus?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_syllabus.html', {'form':form, 'submitted':submitted})

def delete_syllabus(request, syllabus_id):
    syllabus = Course.objects.get(pk=syllabus_id)
    syllabus.delete()
    return redirect('list-syllabus')

def update_syllabus(request, syllabus_id):
    syllabus = Course.objects.get(pk=syllabus_id)
    form = CourseForm(request.POST or None, instance=syllabus)
    if form.is_valid():
        form.save()
        return redirect('list-syllabus')

    return render(request, 'update_syllabus.html', 
    {'syllabus':syllabus, 'form':form})

def search_syllabus(request):
    if request.method == "POST":
        searched = request.POST['searched']
        syllabus = Course.objects.filter(Q(name__contains=searched)|Q(c_code__contains=searched))

        return render(request, 'search_syllabus.html', {'searched':searched, 'syllabus':syllabus})

    else:
        return render(request, 'search_syllabus.html', {})

def list_syllabus(request):
    details_list = Course.objects.all()
    return render(request, 'syllabus.html', 
    {'details_list' : details_list})

def show_syllabus(request, syllabus_id):
    syllabus = Course.objects.get(pk=syllabus_id)
    return render(request, 'show_syllabus.html', 
    {'syllabus' : syllabus})

def home_page(request):
    return render(request, 'homepage.html')

#   Generate PDF File Syllabus Summary
def course_pdf(request, syllabus_id):
    course = Course.objects.get(pk=syllabus_id)

    template_path = 'pdf_convert.html'
    context = {'course': course}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="pdf-convert.pdf'
    template = get_template(template_path)
    html = template.render(context)

   
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
