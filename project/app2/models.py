from django.db import models

# Create your models here.
class actadd(models.Model):
    actadd_id=models.CharField(max_length=90)
    actadd_name=models.CharField(max_length=90)
    actadd_description=models.CharField(max_length=90)
    actadd_status=models.CharField(max_length=90)
    

    class Meta:
        db_table="actadd" 
          
class tbl_volunteer(models.Model):
    tbl_volunteer_id=models.CharField(max_length=90)
    tbl_volunteer_name=models.CharField(max_length=90)
    tbl_volunteer_address=models.CharField(max_length=90)
    tbl_volunteer_age=models.CharField(max_length=90)
    tbl_volunteer_city=models.CharField(max_length=90)
    tbl_volunteer_location=models.CharField(max_length=90)
    tbl_volunteer_email=models.CharField(max_length=90)
    tbl_volunteer_number=models.CharField(max_length=90)
    tbl_volunteer_status=models.CharField(max_length=90)
    tbl_volunteer_photo=models.CharField(max_length=120)
    tbl_volunteer_password=models.CharField(max_length=120)
    tbl_volunteer_aadhaar=models.CharField(max_length=120)



    class Meta:
        db_table="tbl_volunteer"     


class tbl_donor(models.Model):
    tbl_donor_id=models.CharField(max_length=90)
    tbl_donor_name=models.CharField(max_length=90)
    tbl_donor_address=models.CharField(max_length=90)
    tbl_donor_email=models.CharField(max_length=90)
    tbl_donor_phone=models.CharField(max_length=90)
    tbl_donor_aadhaar=models.CharField(max_length=90)
    tbl_donor_status=models.CharField(max_length=90)
    
    class Meta:
         db_table="tbl_donor"   

class tbl_victim(models.Model):
    tbl_victim_id=models.CharField(max_length=90)
    tbl_victim_name=models.CharField(max_length=90)
    tbl_victim_address=models.CharField(max_length=90)
    tbl_victim_email=models.CharField(max_length=90)
    tbl_victim_number=models.CharField(max_length=90)
    tbl_victim_aadhaar=models.CharField(max_length=90)
    tbl_victim_status=models.CharField(max_length=90)
    
    class Meta:
         db_table="tbl_victim"     

class tbl_requestvictim(models.Model):
    tbl_request_id=models.CharField(max_length=90)
    tbl_victim_id=models.CharField(max_length=90)
    tbl_volunteer_id=models.CharField(max_length=90)
    tbl_request=models.CharField(max_length=90)
    tbl_request_date=models.CharField(max_length=90)
    tbl_request_status=models.CharField(max_length=90)   

    class Meta:
        db_table="tbl_requestvictim"    

class tbl_donation(models.Model):
    tbl_donation_id=models.CharField(max_length=90)
    tbl_donor_id=models.CharField(max_length=90)
    tbl_donation=models.CharField(max_length=90)
    tbl_donation_date=models.CharField(max_length=90)
    tbl_request=models.CharField(max_length=90)
    tbl_donation_status=models.CharField(max_length=90)
    
    class Meta:
         db_table="tbl_donation"   

class tbl_allotmenttable(models.Model):
    tbl_allotment_id=models.CharField(max_length=90)
    tbl_request_id=models.CharField(max_length=90)
    tbl_allotment=models.CharField(max_length=90)
    tbl_allotment_date=models.CharField(max_length=90)
    tbl_allotment_status=models.CharField(max_length=90) 

    class Meta:
         db_table="tbl_allotmenttable"

class tbl_login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    category=models.CharField(max_length=90)
    
    class Meta:
         db_table="tbl_login"   


class tbl_publicrequest(models.Model):
    tbl_request_id=models.CharField(max_length=90)
    tbl_volunteer_id=models.CharField(max_length=90)
    tbl_victim_name=models.CharField(max_length=90)
    tbl_victim_address=models.CharField(max_length=90)
    tbl_victim_email=models.CharField(max_length=90)
    tbl_victim_number=models.CharField(max_length=90)
    tbl_request=models.CharField(max_length=90)
    tbl_request_date=models.CharField(max_length=90)
    tbl_public_victim_status=models.CharField(max_length=90)
    tbl_request_aadhaar=models.CharField(max_length=90)
    
    class Meta:
         db_table="tbl_publicrequest"         

