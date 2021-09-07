import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blogproject1.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.random_element(elements=('2021-11-02','2021-10-08','2021-11-12','2021-09-21','2021-12-02','2021-09-28','2021-09-25','2022-01-21','2022-01-19','2021-02-20'))
        fcompany=fake.random_element(elements=('TCS','CTS','INFOSYS','Accenture','Wipro','Capegemini','Hcl','Legato','Tech Mahendra','Bosch','IBM','Global Edge'))
        ftitle=fake.random_element(elements=('project manager','TeamLead','SoftwareEngineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        hydjobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        hydjobs_record=blorejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        hydjobs_record=chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
populate(15)
