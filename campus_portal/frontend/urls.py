from django.urls import path
from .views import main, admin_login, student_login,student_registration,student_dashboard,student_profile,admin_dashboard,view_registered_students,post_drives,available_drives,application_form,applied_students,post_selected_students,selected_students,admin_selected_students,logout
urlpatterns = [
    path('', main, name='main'),
    path('admin-login/', admin_login, name='admin_login'),
    path('student-login/', student_login, name='student_login'),
    path('student-register/',student_registration,name='student_registration'),
    path('student-dashboard/',student_dashboard,name='student_dashboard'),
    path('student-profile/',student_profile,name='student_profile'),
    path('admin-dashboard/',admin_dashboard,name='admin_dashboard'),
    path("view-registered-students/",view_registered_students, name="view_registered_students"),
    path("post-drives/",post_drives, name="post_drives"),
    path("available-drives/",available_drives, name="available_drives"),
    path('application-form/<int:drive_id>/',application_form,name='application_form'),
    path("applied-students/",applied_students, name="applied_students"),
    path("post-selected-students/", post_selected_students, name="post_selected_students"),
    path("selected-students/", selected_students, name="selected_students"),
    path("admin-selected-students/", admin_selected_students, name="admin_selected_students"),
    path('logout/',logout, name='logout'),
    

]
