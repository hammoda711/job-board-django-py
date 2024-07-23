from django.shortcuts import render
from .models import Job
# Create your views here.
def available_jobs(request):
    available_jobs = Job.objects.all()
    context = {
        'available_jobs':available_jobs
    }   
    return render(request,'job/available_jobs.html',context)



def job_details(request,id):
    job_details = Job.objects.get(id=id)
    context = {
        'job_details':job_details
    }
    return render(request,'job/job_details.html',context)
