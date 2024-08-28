from django.shortcuts import redirect,  render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm,PostJobForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.



def available_jobs(request):
    
    available_jobs = Job.objects.all()
   
    # Filter jobs based on the request's query parameters
    myfilter = JobFilter(request.GET, queryset=available_jobs)
    available_jobs = myfilter.qs

    # Paginate the filtered jobs, showing 3 jobs per page
    paginator = Paginator(available_jobs, 3)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Pass the paginated and filtered jobs and the filter itself to the template
    context = {
        'available_jobs':page_obj,
        'myfilter': myfilter
    }   
    return render(request,'job/available_jobs.html',context)


#@login_required
def job_details(request,slug):
    job = Job.objects.get(slug=slug)
    #job_details = get_object_or_404(Job, slug=slug)
    '''
    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.user=request.user
            myform.save()
            return redirect('job:job_details')
    else:
        form= ApplyForm
    '''
    
    
    context = {
        'job_details':job,
        #'form': form
    }
    return render(request,'job/job_details.html',context)


@login_required
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



@login_required
def apply_for_job(request, slug):
    job = get_object_or_404(Job, slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
             # Redirect to the job details page after successful application
            return redirect(reverse('jobs:job_details', kwargs={'slug': job.slug}))
    else:
        form = ApplyForm()

    return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})