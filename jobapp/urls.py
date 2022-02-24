from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/', views.job_index, name='job'),
# Job paths
    path('job/det/<int:job_id>/', views.job_detail, name = 'detail'),
    path('job/create/', views.JobCreate.as_view(), name = 'job_create'),
    path('job/<int:pk>/update/', views.JobUpdate.as_view(), name = 'job_update'),
    path('job/<int:pk>/delete/', views.JobDelete.as_view(), name = 'job_delete'),
# Add contacts
    path('job/<int:job_id>/add_contacts/', views.add_contacts, name = 'add_contacts'),
# checkarks
    path('job/<int:job_id>/checkform/', views.checkform, name = 'checkform'),
# accounts
    path('accounts/signup/', views.signup, name='signup'),
]