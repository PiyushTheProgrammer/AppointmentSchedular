from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils import timezone

class Appointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True, default="Untitled") 
    description = models.TextField(blank=True, null=True)
    appointment_date = models.DateField()  # ✅ Add this
    appointment_time = models.TimeField()  # ✅ Add this
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('appointment_date', 'appointment_time') 

    def __str__(self):
        return f"{self.title} - {self.student.username}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username