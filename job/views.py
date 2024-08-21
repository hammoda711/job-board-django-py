from django.shortcuts import redirect,  render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm,PostJobForm
from django.urls import reverse
#from django.shortcuts import get_object_or_404


# Create your views here.



def available_jobs(request):
    available_jobs = Job.objects.all()
    paginator = Paginator(available_jobs, 3)  # Show 1 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'available_jobs':page_obj
    }   
    return render(request,'job/available_jobs.html',context)



def job_details(request,slug):
    job_details = Job.objects.get(slug=slug)
    #job_details = get_object_or_404(Job, slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form= ApplyForm
    
    
    
    context = {
        'job_details':job_details,
        'form': form
    }
    return render(request,'job/job_details.html',context)



def add_job(request):
    if request.method == 'POST':
        form = PostJobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.employer = request.user
            myform.save()
            return redirect(reverse ('jobs:available_jobs'))
    else:
        form= PostJobForm()


    context={'form': form}
    return render(request,'job/add_job.html',context)