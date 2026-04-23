from django.shortcuts import render

def main(request):
    return render(request, 'frontend/main.html')
def admin_login(request):
    return render(request, 'frontend/admin_login.html')
def student_login(request):
    return render(request, 'frontend/student_login.html')

from django.shortcuts import render, redirect
from .models import Student

def student_registration(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        roll = request.POST.get("roll_number")
        department = request.POST.get("department")
        year = request.POST.get("year")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        # Check duplicate
        if Student.objects.filter(email=email).exists():
            return render(request, "frontend/student_registration.html", {
                "error": "Student already registered"
            })

        Student.objects.create(
            full_name=full_name,
            email=email,
            roll_number=roll,
            department=department,
            year=year,
            password=password,
            phone=phone,
            gender=gender
        )

        return redirect("student_login")

    return render(request, "frontend/student_registration.html")

from django.shortcuts import render,redirect
from.models import Student
def student_login(request):
    if request.method == "POST":
        roll_number = request.POST.get("roll_number").strip()
        password = request.POST.get("password").strip()

        # Authenticate using roll_number
        student = Student.objects.filter(roll_number=roll_number, password=password).first()

        if student:
            # Store roll_number in session
            request.session["roll_number"] = student.roll_number
            return redirect("student_dashboard")
        else:
            return render(request, "frontend/student_login.html", {"error": "Invalid credentials"})

    return render(request, "frontend/student_login.html")

from django.shortcuts import render,redirect
from .models import Student

def student_dashboard(request):
    # Check if student is logged in
    roll_number = request.session.get("roll_number")
    if not roll_number:
        return redirect("student_login")  # redirect to login if not logged in

    # Fetch the student object
    student = Student.objects.filter(roll_number=roll_number).first()
    if not student:
        return redirect("student_login")  # if not found, redirect

    return render(request, "frontend/student_dashboard.html", {
        "student":student
    })

def student_profile(request):
    roll_number = request.session.get("roll_number")

    if not roll_number:
        return redirect("student_login")

    student = Student.objects.filter(roll_number=roll_number).first()
    if not student:
        return redirect("student_login")

    return render(request, "frontend/student_profile.html", {
        "student": student
    })

from django.shortcuts import render,redirect
# Admin login view
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # List of admin users
        admin_users = ["Tajuddin", "Ashma", "Satya", "Meghana", "Rama Rao"]
        admin_password = "Batch2026"

        if username in admin_users and password == admin_password:
            # Save admin session
            request.session["admin_user"] = username
            return redirect("admin_dashboard")
        else:
            return render(request, "frontend/admin_login.html", {"error": "Invalid username or password"})

    return render(request, "frontend/admin_login.html")

from .models import Student

def admin_dashboard(request):
    # Check if admin is logged in
    if "admin_user" not in request.session:
        return redirect("admin_login")
    return render(request, "frontend/admin_dashboard.html")

from django.shortcuts import render, redirect
from .models import Student

def view_registered_students(request):
    # optional: protect admin page
    if "admin_user" not in request.session:
        return redirect("admin_login")

    students = Student.objects.all()

    return render(request, "frontend/view_registered_students.html", {
        "students": students
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Drive, Application

# 1. Page: Post Drive (Admin)
def post_drives(request):
    if request.method == "POST":
        Drive.objects.create(
            company_name=request.POST.get('company_name'),
            eligibility=request.POST.get('eligibility'),
            eligible_branches=",".join(request.POST.getlist('eligible_branches[]')),
            job_type=request.POST.get('job_type'),
            job_role=request.POST.get('job_role'),
            package=request.POST.get('package'),
            process=request.POST.get('process'),
            location=request.POST.get('location'),
            last_date=request.POST.get('last_date'),
        )
        return redirect('admin_dashboard')
    return render(request, 'frontend/post_drives.html')

# 2. Page: Available Drives (Student)
def available_drives(request):
    drives = Drive.objects.all().order_by('-created_at')
    return render(request, 'frontend/available_drives.html', {'drives': drives})

# 3. Page: Application Form (Student)
def application_form(request, drive_id):
    # This fetches the specific drive or shows a 404 error if not found
    drive = get_object_or_404(Drive, id=drive_id)
    
    if request.method == "POST":
        Application.objects.create(
            drive=drive,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            reg_no=request.POST.get('reg_no'),
            mobile=request.POST.get('mobile'),
            branch=request.POST.get('branch'),
            btech_percent=request.POST.get('btech'),
            inter_percent=request.POST.get('inter'),
            ssc_percent=request.POST.get('ssc'),
            resume=request.FILES.get('resume'),
            profile_image=request.FILES.get('image')
        )
        return redirect('student_dashboard')
    return render(request, 'frontend/application_form.html', {'drive': drive})

# 4. Page: Applied Students List (Admin)
def applied_students(request):
    apps = Application.objects.all().order_by('-applied_at')
    return render(request, 'frontend/applied_students.html', {'apps': apps})

from django.shortcuts import render, redirect
from .models import SelectedStudent

def post_selected_students(request):
    if "admin_user" not in request.session:
        return redirect("admin_login")

    if request.method == "POST":
        SelectedStudent.objects.create(
            student_name=request.POST["student_name"],
            register_number=request.POST["register_number"],
            branch=request.POST["branch"],
            company_name=request.POST["company_name"],
            package=request.POST["package"],
            student_photo=request.FILES["student_photo"]
        )
        return redirect("selected_students")

    return render(request, "frontend/post_selected_students.html")

def selected_students(request):
    students = SelectedStudent.objects.all()

    role = "student"
    if "admin_user" in request.session:
        role = "admin"

    return render(request, "frontend/selected_students.html", {
        "students": students,
        "role": role
    })
def admin_selected_students(request):
    students = SelectedStudent.objects.all()

    role = "student"
    if "admin_user" in request.session:
        role = "admin"

    return render(request, "frontend/admin_selected_students.html", {
        "students": students,
        "role": role
    })

def logout(request):
    request.session.flush()
    return render(request, "frontend/logout.html")