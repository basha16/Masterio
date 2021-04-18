from django.shortcuts import render,redirect
from . models import Member
import easygui
from . models import Staffs_data
from django.contrib.auth import logout as auth_logout

# Create your views here.
def instructorlog(request):
    if request.method == 'POST':
        if Member.objects.filter(Username=request.POST['username'], Password=request.POST['password']).exists():
            member = Member.objects.get(Username=request.POST['username'], Password=request.POST['password'])
            return render(request, 'Instructordashboard.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'instructorlog.html', context)  
    else:
        return render(request,'instructorlog.html')

def adminlog(request):
    if request.method == 'POST':
        if Member.objects.filter(Username=request.POST['username'], Password=request.POST['password']).exists():
            member = Member.objects.get(Username=request.POST['username'], Password=request.POST['password'])
            return render(request, 'admindashboard.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'adminlog.html', context)
    else:
        return render(request, 'adminlog.html')

def studentloginpage(request):
    if request.method == 'POST':
        if Member.objects.filter(Username=request.POST['username'], Password=request.POST['password']).exists():
            member = Member.objects.get(Username=request.POST['username'], Password=request.POST['password'])
            return render(request, 'studenthome.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'studentloginpage.html', context)
    else:
        return render(request,'studentloginpage.html')

def instructorRegister_Page(request):
    if request.method == 'POST':
        member = Member(Username=request.POST['username'], Email=request.POST['email'],
                        Password=request.POST['password'])
        member.save()
        easygui.msgbox("your registartion has been completed successfully!...")
        return render(request,'instructorlog.html')
    else:
        return render(request, 'instructorRegister_page.html')

def adminRegister(request):
    if request.method == 'POST':
        member = Member(Username=request.POST['username'], Email=request.POST['email'],
                        Password=request.POST['password'])
        member.save()
        easygui.msgbox("your registartion has been completed successfully!...")
        return render(request,'adminlog.html')
    else:
        return render(request, 'adminRegister.html')

def studentregisterpage(request):
    if request.method == 'POST':
        member = Member(Username=request.POST['username'], Email=request.POST['email'],
                        Password=request.POST['password'])
        member.save()
        easygui.msgbox("your registartion has been completed successfully!...")
        return render(request,'studentloginpage.html')
    else:
        return render(request,'studentregisterpage.html')

def Instructordashboard(request):
    return render(request,'Instructordashboard.html')

def admindashboard(request):
    return render(request,'admindashboard.html') 
    
def index(request):
    return render(request,'index.html')

def Startnewcourse(request):
    return render(request,'Startnewcourse.html') 

def Allcourse(request):
    return render(request,'Allcourse.html') 

def ZoomSetup(request):
    return render(request,'ZoomSetup.html') 

def coursecomments(request):
    return render(request,'coursecomments.html') 

def Allstudents(request):
    return render(request,'Allstudents.html') 

def Messages(request):
    return render(request,'Messages.html') 

def faq2(request):
    return render(request,'faq2.html') 

def Notifications(request):
    return render(request,'Notifications.html') 

def request(request):
    return render(request,'request.html') 

def insNews(request):
    return render(request,'insNews.html')

def logout(request):
    auth_logout(request)
    easygui.msgbox("you are logged out")
    return render(request,"index.html")

def lgout(request):
    auth_logout(request)
    easygui.msgbox("you are logged out")
    return render(request,"index.html")

def Widgets(request):
    return render(request,'Widgets.html') 

def admin_creation(request):
        return render(request,'admin_creation.html',) 

def adinstructors_view(request):
    return render(request,'adinstructors_view.html') 

def adstudent_view(request):
    return render(request,'adstudent_view.html') 

def adshow_category(request):
    return render(request,'adshow_category.html') 

def adshow_courses(request):
    return render(request,'adshow_courses.html') 

def adinstructor_package(request):
    return render(request,'adinstructor_package.html') 

def adminedit_profile(request):
    return render(request,'adminedit_profile.html') 

def admediaprofile(request):
    return render(request,'admediaprofile.html')

def adNewsline(request):
    return render(request,'adNewsline.html')

def adnotification(request):
    return render(request,'adnotification.html')

def adfaq(request):
    return render(request,'adfaq.html')

def studenthome(request):
    return render(request,'studenthome.html')

def adminshow(request):
    s_data=Staffs_data.objects.all()
    return render(request,'adminshow.html', {"s_data":s_data})

def admin_creation(request):
    if request.method == 'POST':
        staffs_data = Staffs_data(Name=request.POST['name'],
        Email=request.POST['email'], Password=request.POST['password'],
        ConfirmPassword=request.POST['cpassword'])
        staffs_data.save()
        easygui.msgbox("Admin has been added successfully.")
        s_data=Staffs_data.objects.all()
        return render(request,'adminshow.html', {"s_data":s_data})
    else:
        return render(request,'admin_creation.html')

def adminedit_creat(request,id):
    staffs_data=Staffs_data.objects.get(id=id)
    return render(request,'adminedit_creat.html',{"s_data":staffs_data})

def staffs_update(request,id):
    staffs_data_edit= Staffs_data(id=id, Name=request.POST['name'],
        Email=request.POST['email'], Password=request.POST['password'],
        ConfirmPassword=request.POST['cpassword'])
    staffs_data_edit.save()
    easygui.msgbox("your staff has been edited successfully.")
    return redirect("adshow")

def staffs_delete(request,id):
    staffs_data=Staffs_data.objects.get(id=id)
    staffs_data.delete()
    easygui.msgbox("your staff has been deleted successfully.")
    return redirect("adshow")   
