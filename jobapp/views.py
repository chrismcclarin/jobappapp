from django.shortcuts import render, redirect
from .models import Job
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import ContactsForm, JobForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/job')
        else:
            error_message = 'invalid credentials - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def checkform(request, job_id):
    form = JobForm(request.POST)
    if form.is_valid():
        checkform = form.save(commit=False)
        checkform.job_id = job_id
        checkform.save()
    return redirect('detail', job_id=job_id)

def home(request):
    return render(request, 'home.html')

@login_required
def job_index(request):
    some_jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/index.html', {'some_jobs': some_jobs})

@login_required
def job_detail(request, job_id):
    some_jobs=Job.objects.filter(user=request.user)
    jobs = Job.objects.get(id=job_id)
    if jobs.user_id != request.user.id:
        return redirect('job')
    checkform= Job
    return render(request, 'jobs/detail.html', {
        'jobs': jobs, 'some_jobs': some_jobs, 'checkform':checkform
        })



class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ('name', 'position', 'date',)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model= Job
    fields = ('name', 'position', 'date', 'resume', 'cover_letter', 'thank_you', 'interview')


class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/job/'

@login_required
def add_contacts(request, job_id):
    form = ContactsForm(request.POST)
    if form.is_valid():
        add_contacts = form.save(commit=False)
        add_contacts.job_id = job_id
        add_contacts.save()
    return redirect('detail', job_id=job_id)
