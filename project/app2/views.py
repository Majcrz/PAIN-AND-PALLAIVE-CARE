from app2.models import actadd
from app2.models import tbl_volunteer
from app2.models import tbl_donor
from app2.models import tbl_victim
from app2.models import tbl_requestvictim
from app2.models import tbl_donation
from app2.models import tbl_publicrequest
from app2.models import tbl_allotmenttable,tbl_login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
import datetime


def adminheader(request):
    return render(request,"admin_header.html")
def adminhome(request):
    return render(request,"adminhome.html")
def volunteerhome(request):
    return render(request,"volunteerhome.html")   
def donorhome(request):
    return render(request,"donorhome.html")     
def logout(request):
    return render(request,"public_header.html")

def activity(request):
    if request.method == 'POST':
        data = actadd()
        data.actadd_id="na"
        data.actadd_name=request.POST.get('activity_name')
        data.actadd_description=request.POST.get('activity_description')
        data.actadd_status="active"
        data.save()
        data.actadd_id="activity_"+str(data.id)
        data.save()

    return render(request,"add_activity.html")

def volunteer(request):
    return render(request,"add_volunteer.html")    
    

def volunteer2(request):
    if request.method == 'POST':
        data = tbl_volunteer()
        data.tbl_volunteer_id="na"
        data.tbl_volunteer_name=request.POST.get('volunteer_name')
        Photo = request.FILES['volunteer_photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)
        data.tbl_volunteer_photo=uploaded_file_url
        data.tbl_volunteer_address=request.POST.get('volunteer_address')
        data.tbl_volunteer_age=request.POST.get('volunteer_age')
        data.tbl_volunteer_city=request.POST.get('volunteer_city')
        data.tbl_volunteer_location=request.POST.get('volunteer_location')
        data.tbl_volunteer_email=request.POST.get('volunteer_email')
        data.tbl_volunteer_number=request.POST.get('volunteer_number')
        data.tbl_volunteer_password=request.POST.get('volunteer_password')
        data.tbl_volunteer_aadhaar=request.POST.get('volunteer_aadhaar')
        data.tbl_volunteer_status="verified"
        data.save()
        data.tbl_volunteer_id="volunteer_"+str(data.id)
        data.save()
        data1=tbl_login()
        data1.username="volunteer_"+str(data.id)
        data1.password=request.POST.get('volunteer_password')
        data1.category="volunteer"
        data1.save()

    return render(request,"add_volunteer.html")
def public(request):
    return render(request,"public_header.html")   

def publicv(request):
    if request.method == 'POST':
        data = tbl_volunteer()
        data.tbl_volunteer_id="na"
        data.tbl_volunteer_name=request.POST.get('volunteer_name')
        Photo = request.FILES['volunteer_photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)
        data.tbl_volunteer_photo=uploaded_file_url
        data.tbl_volunteer_address=request.POST.get('volunteer_address')
        data.tbl_volunteer_age=request.POST.get('volunteer_age')
        data.tbl_volunteer_city=request.POST.get('volunteer_city')
        data.tbl_volunteer_location=request.POST.get('volunteer_location')
        data.tbl_volunteer_email=request.POST.get('volunteer_email')
        data.tbl_volunteer_number=request.POST.get('volunteer_number')
        data.tbl_volunteer_password=request.POST.get('volunteer_password')
        data.tbl_volunteer_aadhaar=request.POST.get('volunteer_aadhaar')
        data.tbl_volunteer_status="Unverified"
        data.save()
        data.tbl_volunteer_id="volunteer_"+str(data.id)
        data.save()
        
    return render(request,"reg_volunteer.html")     
def login(request):
    return render(request,"add_login.html") 
def log(request):
    if request.method == 'POST':
        dataa=tbl_login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        
        flag=0
            
        for da in dataa:
            if un == da.username and pwd == da.password:
                type=da.category
                request.session['uid']=un
                flag = 1
                if type=="admin":
                    return redirect('/adminhome')   
                elif type=="volunteer":
                    
                    return redirect('/volunteerhome')  
                elif type=="donor":
                    
                    return redirect('/donorhome')  
                
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("Invalid user")
def publicd(request):
    if request.method == 'POST':
        data = tbl_donor()
        data.tbl_donor_id="na"
        data.tbl_donor_name=request.POST.get('donor_name')
        data.tbl_donor_address=request.POST.get('donor_address')
        data.tbl_donor_email=request.POST.get('donor_email')
        data.tbl_donor_phone=request.POST.get('donor_phone')
        data.tbl_donor_aadhaar=request.POST.get('donor_aadhaar')
        data.tbl_donor_status="Unverified"
        data.save()
        data.tbl_donor_id="donor_"+str(data.id)
        data.save()
        data1=tbl_login()
        data1.username="donor_"+str(data.id)
        data1.password=request.POST.get('donor_password')
        data1.category="donor"
        data1.save()

    return render(request,"reg_donor.html") 
def volunteer_head(request):
    return render(request,"volunteer_header.html")
def donor(request):
    return render(request,"donor_header.html")  
def victimregistration(request):
    if request.method == 'POST':
        data = tbl_victim()
        data.tbl_victim_id="na"
        data.tbl_victim_name=request.POST.get('victim_name')
        data.tbl_victim_address=request.POST.get('victim_address')
        data.tbl_victim_email=request.POST.get('victim_email')
        data.tbl_victim_number=request.POST.get('victim_number')
        data.tbl_victim_aadhaar=request.POST.get('victim_aadhaar')
        data.tbl_victim_status="not_allotted"
        data.save()
        data.tbl_victim_id="applicant_"+str(data.id)
        data.save()
        
    return render(request,"victim_registration.html") 
def removevolunteer(request):
    items = tbl_volunteer.objects.filter(tbl_volunteer_status="verified")
    return render(request,"remove_volunteer.html",{'items':items }) 

def delete_volunteer(request, id):
    items = tbl_volunteer.objects.get(id=id)    
    items.delete()
    items1=tbl_login.objects.get(username=items.tbl_volunteer_id)
    items1.delete()
    return redirect('/removevolunteer')

def removeactivity(request):
    items = actadd.objects.all()
    return render(request,"remove_activity.html",{'items':items }) 

def delete_activity(request, id):
    items = actadd.objects.get(id=id)    
    items.delete()
    return redirect('/removeactivity')

def verifyvolunteer(request):
    items = tbl_volunteer.objects.filter(tbl_volunteer_status="Unverified")
    return render(request,"verify_volunteer.html",{'items':items }) 

def verifyvolunteer1(request, id):
    items = tbl_volunteer.objects.get(id=id)   
    items.tbl_volunteer_status="verified"
    items.save()
    data1=tbl_login()
    data1.username=items.tbl_volunteer_id
    data1.password=items.tbl_volunteer_password
    data1.category="volunteer"
    data1.save()
    return redirect('/verifyvolunteer')   

def viewdonor1(request):
    items = tbl_donor.objects.all()
    return render(request,"view_donor.html",{'items':items }) 

def delete_donor(request, id):
    items = tbl_donor.objects.get(id=id)    
    items.delete()
    return redirect('/viewdonor1')  

def requestvictim(request):
    items = tbl_victim.objects.filter(tbl_victim_status="not_allotted")
    return render(request,"request_victimreg.html",{'items':items }) 

def requestvictim2(request, id):
    items = tbl_victim.objects.get(id=id)   
    uid=request.session['uid']
    return render(request,"requestvictim.html",{'items1':items,'uid':uid})    

def requestvictim3(request):
    return render(request,"requestvictim.html")    
    

def requestvictim4(request):
    if request.method == 'POST':
        data = tbl_requestvictim()
        data.tbl_request_id="na"
        data.tbl_victim_id=request.POST.get('victim_id')
        data.tbl_volunteer_id=request.POST.get('volunteer_id')
        data.tbl_request=request.POST.get('request')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.tbl_request_date=time1
        data.tbl_request_status="pending"
        data.save()
        data.tbl_request_id="request_"+str(data.id)
        data.save()
        data1=tbl_victim.objects.get(tbl_victim_id=request.POST.get('victim_id'))   
        data1.tbl_victim_status="requested"
        
        data1.save()

    return redirect('/requestvictim')

def viewactivities(request):
    items = actadd.objects.all()
    return render(request,"view_activities.html",{'items':items })    

def viewrequest(request):
    items = tbl_victim.objects.filter(tbl_victim_status="requested")
    return render(request,"view_request.html",{'items':items }) 

def viewrequest2(request,id):
    items = tbl_requestvictim.objects.filter(tbl_victim_id=id)   
    return render(request,"view_request2.html",{'items2':items})   

def viewrequest3(request,id):
    items = tbl_donation.objects.filter(tbl_donation_id=id)   
    uid=request.session['uid']
    return render(request,"donation_request.html",{'items2':items,'uid':uid})

def donation3(request):
    return render(request,"donation_request.html")    


def donation4(request):
    if request.method == 'POST':
        data = tbl_donation()
        data.tbl_donation_id="na"
        data.tbl_donor_id=request.POST.get('donor_id')
        data.tbl_donation=request.POST.get('donation')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.tbl_donation_date=time1
        data.tbl_donation_status="pending"
        data.save()
        data.tbl_donation_id="request_"+str(data.id)
        data.save()      
    return redirect('/viewrequest')
    
def viewactivitiesp(request):
    items = actadd.objects.all()
    return render(request,"view_activitiesp.html",{'items':items })             

def viewdonor2(request):
    items = tbl_donor.objects.all()
    return render(request,"viewdonation0.html",{'items':items })   
           
def viewrequest5(request,id):
    items = tbl_donation.objects.filter(tbl_donor_id=id)   
    return render(request,"donation.html",{'items2':items})   

def requestprocess(request):
    items = tbl_volunteer.objects.filter(tbl_volunteer_status="verified")
    return render(request,"requestprocess.html",{'items':items })      

def requestprocess1(request,id):
    items = tbl_requestvictim.objects.all()   
    return render(request,"requestprocess1.html",{'items2':items})     

def allotment1(request,id):  
    return render(request,"allotment.html")    

def allotmenttable(request):
    if request.method == 'POST':
        data = tbl_allotmenttable()
        data.tbl_allotment_id="na"
        data.tbl_request_id=request.POST.get('request_id')
        data.tbl_allotment=request.POST.get('allotment')
        data.tbl_allotment_date=request.POST.get('allotment_date')
        data.tbl_allotment_status="pending"
        data.save()     
        data.tbl_allotment_id="allotment_"+str(data.id)
        data.save()  
    return render(request,"allotment.html")

def allotment5(request, id):
    items = tbl_requestvictim.objects.get(id=id)   
    items.tbl_request_status="rejected"
    items.save()
    return redirect('/requestprocess')
def viewvolunteer(request,id):
    items = tbl_volunteer.objects.get(tbl_volunteer_id=id)
    return render(request,"viewvolunteer.html",{'ct':items })     

def reportdonor(request):
    items = tbl_donor.objects.all()
    return render(request,"adminreport.html",{'items':items })          
 
def reportdonorview(request,id):
    items = tbl_donation.objects.filter(tbl_donor_id=id)   
    return render(request,"reportdonorview.html",{'items2':items})

def reportrequest(request):
    items = tbl_requestvictim.objects.all()
    return render(request,"reportrequest.html",{'items':items })  

def volunteerallot(request):
    items = tbl_requestvictim.objects.all()
    return render(request,"volunteerallot.html",{'items':items })    

def volunteerallot1(request,id):
    items = tbl_allotmenttable.objects.all()   
    return render(request,"volunteerallot1.html",{'items2':items}) 

def publicrequestview(request):
    items = tbl_requestvictim.objects.all() 
    return render(request,"publicrequestview.html",{'items2':items})    

def publicrequest(request):
    return render(request,"publicrequest.html")   

def publicrequest1(request):
    if request.method == 'POST':
        data = tbl_publicrequest()
        data.tbl_request_id="na"
        data.tbl_volunteer_id="null"
        data.tbl_victim_name=request.POST.get('victim_name')
        data.tbl_victim_address=request.POST.get('victim_address')
        data.tbl_victim_email=request.POST.get('victim_email')
        data.tbl_victim_number=request.POST.get('victim_number')
        data.tbl_request_aadhaar=request.POST.get('request_aadhaar')
        data.tbl_request=request.POST.get('request')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.tbl_request_date=time1
        data.tbl_public_victim_status="not_Verified"
        data.save()
        data.tbl_victim_id="public_applicant_"+str(data.id)
        data.save()  
        data.tbl_request_id="public_request_"+str(data.id)
        data.save() 

    return render(request,"publicrequest.html") 

def verifyrequest(request):
    items = tbl_publicrequest.objects.filter(tbl_public_victim_status="not_Verified")
    return render(request,"verifyrequest.html",{'items':items })      

def verifyrequest1(request, id):
    items = tbl_publicrequest.objects.get(id=id)   
    items.tbl_public_victim_status="Rejected"
    items.save()
    return redirect('/verifyrequest')    

def verifyrequest2(request, id):
    request.session['pid']=id
    items = tbl_volunteer.objects.filter(tbl_volunteer_status="verified")
    return render(request,"verifyrequest1.html",{'items2':items })     


def verifyrequest3(request, id):
    pid = request.session['pid']
    items = tbl_publicrequest.objects.get(id=pid)
    items.tbl_volunteer_id=id
    items.tbl_public_victim_status="verified"
    items.save()
    return redirect('/verifyrequest')




          
 






      




# Create your views here.