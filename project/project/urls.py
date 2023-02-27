"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app2 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminheader/',views.adminheader),
    path('adminhome/',views.adminhome),
    path('volunteerhome/',views.volunteerhome),
    path('donorhome/',views.donorhome),
    path('activity/',views.activity),
    path('logout/',views.logout),
    path('volunteer/',views.volunteer),
    path('public/',views.public),
    path('publicv/',views.publicv),
    path('login/',views.login),
    path('publicd/',views.publicd),
    path('volunteer_head/',views.volunteer_head),
    path('donor/',views.donor),
    path('victimregistration/',views.victimregistration),
    path('removevolunteer/',views.removevolunteer),
    path('delete_volunteer/<int:id>',views.delete_volunteer),
    path('removeactivity/',views.removeactivity),
    path('delete_activity/<int:id>',views.delete_activity),
    path('verifyvolunteer/',views.verifyvolunteer),
    path('verifyvolunteer1/<int:id>',views.verifyvolunteer1),
    path('viewdonor1/',views.viewdonor1),
    path('delete_donor/<int:id>',views.delete_donor),
    path('volunteer2/',views.volunteer2),
    path('requestvictim/',views.requestvictim),
    path('requestvictim2/<int:id>',views.requestvictim2),
    path('requestvictim3/',views.requestvictim3),
    path('requestvictim4/',views.requestvictim4),
    path('viewactivities/',views.viewactivities),
    path('viewrequest/',views.viewrequest), 
    path('viewrequest2/<str:id>',views.viewrequest2),  
    path('viewrequest3/<str:id>',views.viewrequest3),
    path('donation3/',views.donation3),     
    path('donation4/',views.donation4),
    path('viewactivitiesp/',views.viewactivitiesp),
    path('viewdonor2/',views.viewdonor2),
    path('viewrequest5/<str:id>',views.viewrequest5),
    path('requestprocess/',views.requestprocess),
    path('requestprocess1/<str:id>',views.requestprocess1),
    path('allotment1/<int:id>',views.allotment1),
    path('allotmenttable/',views.allotmenttable),
    path('allotment5/<int:id>',views.allotment5),
    path('log/',views.log),
    path('viewvolunteer/<str:id>',views.viewvolunteer),
    path('reportdonor/',views.reportdonor),
    path('reportdonorview/<str:id>',views.reportdonorview),
    path('reportrequest/',views.reportrequest),
    path('volunteerallot/',views.volunteerallot),
    path('volunteerallot1/<str:id>',views.volunteerallot1),
    path('publicrequestview/',views.publicrequestview),
    path('publicrequest/',views.publicrequest),
    path('publicrequest1/',views.publicrequest1),
    path('verifyrequest/',views.verifyrequest),
    path('verifyrequest1/<int:id>',views.verifyrequest1),
    path('verifyrequest2/<int:id>',views.verifyrequest2),
    path('verifyrequest3/<str:id>',views.verifyrequest3),



    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)