from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.



def available_jobs(request):
    available_jobs = Job.objects.all()
    paginator = Paginator(available_jobs, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'available_jobs':page_obj
    }   
    return render(request,'job/available_jobs.html',context)



def job_details(request,id):
    job_details = Job.objects.get(id=id)
    context = {
        'job_details':job_details
    }
    return render(request,'job/job_details.html',context)
