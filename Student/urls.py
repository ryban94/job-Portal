from django.urls import path
from Student import views

urlpatterns = [
    path('main_page/', views.main_page, name="main_page"),
    path('recruiter/', views.recruiter, name="recruiter"),
    path('placement/', views.placement, name="placement"),
    path('training/', views.training, name="training"),
    path('gallery/', views.gallery, name="gallery"),
    path('help/', views.help, name="help"),
    path('contact/', views.contact, name="contact"),
    
    path('index/', views.indexpage, name="indexpage"),
    path('stud_profile/',views.stud_profile,name="stud_profile"),
    path('stud_edit/',views.stud_edit,name="stud_edit"),
    path('stud_save/',views.stud_save,name="stud_save"),
    path('stud_notification/',views.stud_notification,name="stud_notification"),
    path('stud_user/',views.stud_user,name="stud_user"),
    path('stud_login/',views.stud_login,name="stud_login"),
    path('stud_save/',views.stud_save,name="stud_save"),
    path('stud_logout/',views.stud_logout,name="stud_logout"),
    path('jobs_view/', views.jobs_view, name="jobs_view"),
    path('jobs_view_single/<int:job_id>/', views.jobs_view_single, name="jobs_view_single"),
    path('job_apply/<int:job_id>/', views.job_apply, name="job_apply"),
    path('main_login/', views.main_login, name="main_login"),


]