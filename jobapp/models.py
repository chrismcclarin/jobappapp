from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms

class Job(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.DateField()
    resume = models.BooleanField(default=False, editable=True)
    cover_letter= models.BooleanField(default=False, editable=True)
    thank_you = models.BooleanField(default=False, editable=True)
    interview = models.BooleanField(default=False, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id})

class Contacts(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.DateField()
    thank_you= models.BooleanField()
