from django.db import models
from django.contrib.auth.models import User
#for signal
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE , blank=True, null=True)
    phone_number = models.CharField(max_length=17)
    image = models.ImageField(upload_to='profile/')

    
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Employer', 'Employer'),
        ('Employee', 'Employee'),
    ]
    
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    # Define USER_ROLES for use in forms
    USER_ROLES = ROLE_CHOICES

    def __str__(self):
        return str(self.user)


#django signal 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class City(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name