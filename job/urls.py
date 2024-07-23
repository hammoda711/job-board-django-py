from django.urls import path,include
from . import views
urlpatterns = [
    #we use '' because it the project url for jobs app includes 'jobs/' so no need to use another 
    path('',views.available_jobs), 
    #here we need to use id to handle specific job so we use '<int:id>' 
    path('<int:id>',views.job_details)
]
