# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

from django.contrib.auth.models import User

from datetime import datetime

from django.contrib.auth.models import User
from django.conf import settings
#"Aparty", "BParty","Datetime","Duration","cellid","Imei","Imsi","type","CallType","SiteLocation"]
# Create your models here.


class Cases(models.Model):
    id = models.AutoField(primary_key=True)
    #req
    casetype = models.CharField(max_length=150)
    fir = models.CharField(max_length=150,null=True, blank=True)
    ps= models.CharField(max_length=150,null=True, blank=True)
    telco= models.CharField(max_length=150,null=True, blank=True)
    voip= models.CharField(max_length=150,null=True, blank=True)
    complaintcaste= models.CharField(max_length=150,null=True, blank=True)
    modusoperandus= models.CharField(max_length=150,null=True, blank=True)
    #req
    casetitle= models.CharField(max_length=150)
    #casedate= models.DateTimeField(max_length=150)
    #req
    casedate= models.CharField(max_length=150)
    region= models.CharField(max_length=650,null=True, blank=True)
    internationalno= models.CharField(max_length=150,null=True, blank=True)
    coplaintname= models.CharField(max_length=650,null=True, blank=True)
    profession= models.CharField(max_length=150,null=True, blank=True)
    #incidentdate= models.DateTimeField(max_length=150)
    #req
    incidentdate= models.CharField(max_length=150)
    #req
    firreference= models.CharField(max_length=150)
    us= models.CharField(max_length=650,null=True, blank=True)
    localno= models.CharField(max_length=150,null=True, blank=True)
    country= models.CharField(max_length=150,null=True, blank=True)
    complaintno= models.CharField(max_length=150,null=True, blank=True)
    groupclaim= models.CharField(max_length=150,null=True, blank=True)
    incidenttime= models.TimeField(auto_now=False, auto_now_add=False, max_length=150)
    createdat = models.DateTimeField(default=datetime.now, blank=True)
    incident_ps_jurisdiction = models.CharField(max_length=150,null=True, blank=True)
    demand_amount = models.CharField(max_length=150,null=True, blank=True)
    victim_reference = models.CharField(max_length=150,null=True, blank=True)
    victim = models.CharField(max_length=150,null=True, blank=True)
    io = models.CharField(max_length=150,null=True, blank=True)
    incident_place= models.CharField(max_length=150,null=True, blank=True)
    remarks = models.CharField(max_length=150,null=True, blank=True)
    #userid = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    class Meta:  
        db_table = "cases"

class CDRList(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=150,null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    operator = models.CharField(max_length=150,null=True, blank=True)
    caseid = models.ForeignKey(Cases, on_delete=models.CASCADE,default=1)

    
    class Meta:  
        db_table = "cdrlist"

class BTSList(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=150,null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    operator = models.CharField(max_length=150,null=True, blank=True)
    caseid = models.ForeignKey(Cases, on_delete=models.CASCADE,default=1)

    
    class Meta:  
        db_table = "btslist"


class CDR(models.Model):
    id = models.AutoField(primary_key=True)
    aparty = models.CharField(max_length=150,null=True, blank=True)
    bparty = models.CharField(max_length=150,null=True, blank=True)
    ts= models.CharField(max_length=150,null=True, blank=True)
    duration= models.CharField(max_length=150,null=True, blank=True)
    cellid= models.CharField(max_length=150,null=True, blank=True)
    imei= models.CharField(max_length=150,null=True, blank=True)
    imsi= models.CharField(max_length=150,null=True, blank=True)
    calltype = models.CharField(max_length=150,null=True, blank=True)

    lacid = models.CharField(max_length=150,null=True, blank=True)
    servicetype = models.CharField(max_length=150,null=True, blank=True)
    cellsector = models.CharField(max_length=150,null=True, blank=True)
    operator = models.CharField(max_length=150,default="")

    direction = models.CharField(max_length=150,null=True, blank=True)
    SiteAddress= models.CharField(max_length=650,null=True, blank=True)
    source = models.CharField(max_length=150,default="")
    destination = models.CharField(max_length=150,default="")
    caseid = models.ForeignKey(Cases, on_delete=models.CASCADE,default=1)
    cdrlist = models.ForeignKey(CDRList, on_delete=models.CASCADE,default=1)
   
    class Meta:  
        db_table = "cdr"


class BTS(models.Model):
    id = models.AutoField(primary_key=True)
    aparty = models.CharField(max_length=150,null=True, blank=True)
    bparty = models.CharField(max_length=150,null=True, blank=True)
    ts= models.CharField(max_length=150,default="")
    duration= models.CharField(max_length=150,null=True, blank=True)

    cellid= models.CharField(max_length=150,default="")
    imei= models.CharField(max_length=150,default="")
    imei2= models.CharField(max_length=150,default="")
    imsi= models.CharField(max_length=150,default="")
    calltype = models.CharField(max_length=150,default="")

    lacid = models.CharField(max_length=150,default="")
    servicetype = models.CharField(max_length=150,default="")
    cellsector = models.CharField(max_length=150,default="")
    operator = models.CharField(max_length=150,default="")

    direction = models.CharField(max_length=150,default="")
    SiteAddress= models.CharField(max_length=650,default="")
    source = models.CharField(max_length=150,default="")
    destination = models.CharField(max_length=150,default="")
    caseid = models.ForeignKey(Cases, on_delete=models.CASCADE,default=1)
    cdrlist = models.ForeignKey(BTSList, on_delete=models.CASCADE,default=1)
   
    class Meta:  
        db_table = "bts"

