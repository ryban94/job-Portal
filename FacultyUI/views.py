from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError



from AdminUI.models import StudentDB, CourseDB, FacultyEnrollmentDB, DepartmentDB
from FacultyUI.models import FacultyDB
import Student.views
import AdminUI.views


# Create your views here.
def login_page(request):
    return render(request, "login.html")


def faculty_login(request):
    if request.method == "POST":
        uid = request.POST.get("userid")
        mob = request.POST.get("pass")
        if FacultyEnrollmentDB.objects.filter(FacultyID=uid, Contact=mob).exists():
            request.session["username"] = uid
            request.session["password"] = mob
            if FacultyEnrollmentDB.objects.get(FacultyID=uid).is_admin == True:
                return redirect(AdminUI.views.admin_indexpage)
            else:
                return redirect(index_page)
        else:
            return redirect(Student.views.main_login)


def get_enrollment_data(request):
    if 'username' in request.session:
        fid = request.session["username"]
        f_data = FacultyEnrollmentDB.objects.get(FacultyID=fid)
        return f_data


def get_faculty_data(request):
    if 'username' in request.session:
        fid = request.session["username"]
        f_data = FacultyDB.objects.get(FacultyID=fid)
        return f_data


def filter_faculty_data(request):
    if 'username' in request.session:
        fid = request.session["username"]
        f_data = FacultyDB.objects.filter(FacultyID=fid)
        return f_data


def filter_enrollment_data(request):
    if 'username' in request.session:
        fid = request.session["username"]
        f_data = FacultyEnrollmentDB.objects.filter(FacultyID=fid)
        return f_data


def index_page(request):
    enroll_data = get_enrollment_data(request)
    if filter_faculty_data(request).exists():
        f_data = get_faculty_data(request)
    else:
        f_data = None
    return render(request, "faculty_index.html", {'enroll_data': enroll_data, 'f_data': f_data})


def profile_page(request):
    enroll_data = get_enrollment_data(request)
    dept_data = DepartmentDB.objects.get(DeptId=enroll_data.DeptId.DeptId)
    print(dept_data)
    if filter_faculty_data(request).exists():
        f_data = get_faculty_data(request)
    else:
        f_data = None
    return render(request, "faculty_profile.html",
                  {'f_data': f_data, 'enroll_data': enroll_data, 'dept_data': dept_data})


def profile_edit(request):
    enroll_data = get_enrollment_data(request)
    if filter_faculty_data(request).exists():
        f_data = get_faculty_data(request)
        return render(request, "faculty_profile_edit.html", {'f_data': f_data, 'enroll_data': enroll_data})
    else:
        return render(request, "faculty_profile_edit.html", {'enroll_data': enroll_data})



def profile_save(request):
    if request.method == "POST":
        f_data = get_enrollment_data(request)
        fid = request.POST.get("id")
        name = request.POST.get("name")
        jdate = f_data.Joined
        dob = request.POST.get("dob")
        cont = request.POST.get("contact")
        altcont = request.POST.get("altcontact")
        addr = request.POST.get("address")
        mail = request.POST.get("email")
        bname = request.POST.get("bank")
        accnum = request.POST.get("accnum")
        ifsc = request.POST.get("ifsc")
        if filter_faculty_data(request).exists():
            try:
                img = request.FILES["image"]
                fs = FileSystemStorage()
                file = fs.save(img.name, img)
            except MultiValueDictKeyError:
                file = get_faculty_data(request).Photo
            FacultyDB.objects.filter(FacultyID=fid).update(
                DoB=dob, AltContact=altcont,
                Address=addr, Email=mail, Bank=bname, Acc_Number=accnum,
                IFSC=ifsc, Photo=file)
            FacultyEnrollmentDB.objects.filter(FacultyID=fid).update(Name=name, Contact=cont)
        else:
            img = request.FILES["image"]
            obj = FacultyDB(FacultyID_id=f_data.FacultyID.FacultyID,
                            DoB=dob, AltContact=altcont,
                            Address=addr, Email=mail, Bank=bname, Acc_Number=accnum,
                            IFSC=ifsc, Photo=img)
            obj.save()
            FacultyEnrollmentDB.objects.filter(FacultyID=fid).update(Name=name, Contact=cont)
        messages.success(request, "Profile Updated")
        return redirect(profile_page)


def students_view(request):
    data = CourseDB.objects.all()
    stud_data = StudentDB.objects.all()
    years = []
    for i in stud_data:
        year = i.EnrollDate.year
        years.append(year)
    return render(request, "faculty_student_view.html", {"data": data, "years": years})


def search_students(request):
    if request.method == "POST":
        course = request.POST.get("course")
        course_data = CourseDB.objects.get(CourseName=course)
        cours = course_data.CourseId
        year = request.POST.get("year")
        data = StudentDB.objects.filter(CourseId=cours, EnrollDate__year=year)
        return render(request, "faculty_student_search.html", {"data": data, "course": course})


def student_single(request, dataid):
    s_data = StudentDB.objects.get(StudentId=dataid)
    course = CourseDB.objects.get(CourseId=s_data.CourseId.CourseId)
    return render(request, "faculty_student_single.html", {'s_data': s_data, 'course': course})


def faculty_logout(request):
    if request.session["username"].isdigit():
        f_data = filter_enrollment_data(request)
        get_f_data = get_enrollment_data(request)
        del request.session["username"]
        del request.session["password"]
        messages.success(request, "Log Out Success")
        if get_f_data.is_admin != True:
            return redirect(login_page)
        else:
            return redirect(login_page)
    else:
        del request.session["username"]
        del request.session["password"]
        return redirect(AdminUI.views.admin_login)
