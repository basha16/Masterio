from django.urls import path

from . import views

urlpatterns=[
    path('instructorlog/',views.instructorlog,name='insloginpage'),
    path('instructorRegister_Page/',views.instructorRegister_Page,name='insregister_page'),
    path('adminlog/',views.adminlog,name='adminloginpage'),
    path('adminRegister/',views.adminRegister,name='adminregister'),
    path('studentloginpage/',views.studentloginpage,name='stloginpage'),
    path('studentregisterpage/',views.studentregisterpage,name='stregisterpage'),
    path('Instructordashboard/',views.Instructordashboard,name='insdashboard'),
    path('admindashboard/',views.admindashboard,name='addashboard'),
    path('',views.index,name='index'),
    path('Startnewcourse/',views.Startnewcourse,name='newcourse'),
    path('Allcourse/',views.Allcourse,name='allcourse'),
    path('ZoomSetup/',views.ZoomSetup,name='zoomset'),
    path('coursecomments/',views.coursecomments,name='comments'),
    path('Allstudents/',views.Allstudents,name='allstudents'),
    path('Messages/',views.Messages,name='message'),
    path('faq2/',views.faq2,name='faq2'),
    path('Notifications',views.Notifications,name='notifi'),
    path('request/',views.request,name='req'),
    path('insNews/',views.insNews,name='insnews'),
    path('logout/',views.logout,name='logout'),
    path('Widgets/',views.Widgets,name='widgets'),
    path('admin_creation/',views.admin_creation,name='adcreation'),
    path('adinstructors_view/',views.adinstructors_view,name='insview'),
    path('adstudent_view/',views.adstudent_view,name='adstview'),
    path('adshow_category/',views.adshow_category,name='adshowcat'),
    path('adshow_courses/',views.adshow_courses,name='adshowcourse'),
    path('adinstructor_package/',views.adinstructor_package,name='adinstructorpackage'),
    path('adminedit_profile/',views.adminedit_profile,name='adeditprofile'),
    path('admediaprofile/',views.admediaprofile,name='admediapro'),
    path('adNewsline/',views.adNewsline,name='NewsLine'),
    path('adnotification/',views.adnotification,name='adnotifi'),
    path('adfaq/',views.adfaq,name='faq'),
    path('adminshow/',views.adminshow,name='adshow'),
    path('lgout/',views.lgout,name='lgout'),
    path('studenthome/',views.studenthome,name='stuhome'),
    path('adminedit_creat/<int:id>',views.adminedit_creat, name="admin_Edit"),
    path('staffs_update/<int:id>',views.staffs_update, name="staffs_update"),
    path('staffs_delete/<int:id>',views.staffs_delete, name="staffs_delete"),
]