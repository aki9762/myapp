# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class pcontentsid(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def pcontentid():
               try:
                        uuid = pcontentsid.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = pcontentsid()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               groupID = 'PCID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return groupID
			   
class pagecontent(models.Model):
  pcid=models.CharField(default=pcontentid, max_length=200, unique=True)
  name=models.TextField(null=True,blank=True)
  desc=models.TextField(null=True,blank=True)
  showdesc=models.BooleanField(default=True)
  pcontent=models.TextField(null=True,blank=True)
  displayname=models.BooleanField(default=True)
  displaydesc=models.BooleanField(default=True)
  tracking=models.CharField(max_length=128)
  requireviewactivity=models.BooleanField(default=True)
  recivegradetocomplete=models.BooleanField(default=True)
  submittocomplete=models.BooleanField(default=True)
  completedondate=models.DateField(null=True,blank=True)
  tags=models.TextField(null=True,blank=True)
  coursecompitancies=models.CharField(max_length=128)
  uponactivitycompitancy=models.CharField(max_length=128)
  isActive=models.BooleanField(default=True)
  createdBy=models.ForeignKey(User, related_name="pagecontentCreatedBy", null= True)
  modifiedBy=models.ForeignKey(User, related_name="pagecontentModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  def __unicode__(self):
    return self.name