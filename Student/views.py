from datetime import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from AdminUI.models import StudentDB, DepartmentDB, CourseDB,JobsDB,JobApplications,newsDB
import FacultyUI.views
import AdminUI.views


# Create your views here.
def main_login(request):
    
    return render(request,"main_login.html")

def main_page(request):
    stud_id = request.session.get("username")
    last_post = newsDB.objects.latest('newsId')
    recent_posts = newsDB.objects.order_by('newsId')[1:5]
    job_data=JobsDB.objects.all()
    if stud_id:
        name = StudentDB.objects.get(StudentId=stud_id)
        return render(request,"main_home.html",{"name":name,"job_data":job_data,"last_post":last_post,"recent_posts":recent_posts})
    else:
        return render(request,"main_home.html",{"job_data":job_data,"last_post":last_post,"recent_posts":recent_posts})

def recruiter(request):
    stud_id = request.session.get("username")
    job_data=JobsDB.objects.all()
    if stud_id:
        name = StudentDB.objects.get(StudentId=stud_id)
        return render(request,"1_recruiter.html",{"name":name,'job_data':job_data})
    else:
        return render(request,"1_recruiter.html",{'job_data':job_data})


def placement(request):
    stud_id = request.session.get("username")
    if stud_id:
        name = StudentDB.objects.get(StudentId=stud_id)
        return render(request,"2_placement.html",{"name":name})
    else:
        return render(request,"2_placement.html")

def training(request):
    return render(request,"3_trainingt.html")

def gallery(request):
    return render(request,"4_gallery.html")


def contact(request):
    return render(request,"6_contact.html")

def indexpage(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request, "studentindex.html", {'name': name, 'course': course, 'dept': dept})


def stud_profile(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request, "student_profile.html", {'name': name, 'course': course, 'dept': dept})


def stud_edit(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request, "student_edit.html", {'name': name, 'course': course, 'dept': dept})


def stud_save(request):
    if request.method == "POST":
        stud_id = request.POST.get('StudentId')
        stud_fname = request.POST.get('FirstName')
        stud_lname = request.POST.get('LastName')
        stud_dob = request.POST.get('DateOfBirth')
        date_objj = datetime.strptime(stud_dob, "%B %d, %Y")
        formatted_dob = date_objj.strftime("%Y-%m-%d")

        stud_gender = request.POST.get('Gender')
        stud_email = request.POST.get('Email')
        stud_mob = request.POST.get('ContactNo')
        stud_address = request.POST.get('Address')
        stud_gcontact = request.POST.get('GuardianContact')
        stud_gname = request.POST.get('GuardianName')
        stud_dept = request.POST.get('DeptName')
        stud_course = request.POST.get('CourseName')
        try:
            stud_image = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(stud_image.name, stud_image)
        except MultiValueDictKeyError:
            file = StudentDB.objects.get(StudentId=stud_id).Image
            print(file)
        if StudentDB.objects.filter(StudentId=stud_id).exists():
            StudentDB.objects.filter(StudentId=stud_id).update(FirstName=stud_fname, LastName=stud_lname,
                                                               DateOfBirth=formatted_dob, Gender=stud_gender,
                                                               Email=stud_email, ContactNo=stud_mob,
                                                               Address=stud_address,
                                                               GuardianContact=stud_gcontact, GuardianName=stud_gname,
                                                               Image=file)
        else:
            stud_image = request.FILES['Image']
            obj = StudentDB(FirstName=stud_fname, LastName=stud_lname,
                            DateOfBirth=stud_dob, Gender=stud_gender,
                            Email=stud_email, ContactNo=stud_mob, Address=stud_address,
                            GuardianContact=stud_gcontact, GuardianName=stud_gname,
                            Image=stud_image)
            obj.save()
        return redirect(stud_profile)


def stud_notification(request):
    obj=newsDB.objects.all()
    return render(request,'notification.html',{"obj":obj})


def stud_user(request):
    return render(request, 'student_login.html')


def stud_login(request):
    if request.method == "POST":
        stud_id = request.POST.get('userid')
        stud_pwd = request.POST.get('pass')
        if StudentDB.objects.filter(StudentId=stud_id, ContactNo=stud_pwd).exists():
            request.session['username'] = stud_id
            request.session['password'] = stud_pwd
            messages.success(request, "Login successfully")
            return redirect(main_page)
        else:
            messages.error(request, "Invalid ID or Password")
            return redirect(main_login)
    else:
        messages.error(request, "Invalid ID or Password")
        return redirect(main_login)


def stud_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(main_page)




def jobs_view(request):
    job_data=JobsDB.objects.all()
    return render(request,"jobs_view.html",{'job_data':job_data})


def jobs_view_single(request, job_id):
    if 'username' in request.session:
        stud_id = request.session["username"]
        job_data = JobsDB.objects.get(JobId=job_id)
        applied = JobApplications.objects.filter(JobId=job_id, StudentId=stud_id).exists()
        # messages.success(request, 'You have successfully applied for the job!')
        return render(request, "job_view_single.html", {'job_data': job_data, 'applied': applied})
    else:
        messages.error(request, 'Please log in to view this page.')
        return render(request, "main_login.html")


def job_apply(request,job_id):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    job = JobsDB.objects.get(JobId=job_id)
    resume = request.FILES["resume"]
    obj=JobApplications(JobId=job,StudentId=name,Resume=resume)
    obj.save()
    return redirect(jobs_view)

def notification_single(request,news_id):
    news_data= newsDB.objects.get(newsId=news_id)
    return render(request,"notification_single.html",{"news_data":news_data})


def help(request):
    return render(request,'5_help.html')

