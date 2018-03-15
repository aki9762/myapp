# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class groupUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getgroupId():
               try:
                        uuid = groupUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = groupUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               groupID = 'groupID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return groupID
			   
class format_type(models.Model):
  fId=models.CharField(default=getgroupId, max_length=200, unique=True)
  name=models.TextField(null=True,blank=True)  
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.name

class sUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getacttypid():
               try:
                        uuid = sUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = sUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               groupID = 'ACTID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return groupID

class single_activity_type(models.Model):
  actid=models.CharField(default=getacttypid, max_length=200, unique=True)
  name=models.TextField(null=True,blank=True)  
  isActive=models.BooleanField(default=True)
  createdBy=models.ForeignKey(User, related_name="subjectGroupCreatedBy", null= True)
  modifiedBy=models.ForeignKey(User, related_name="subjectGroupModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  def __unicode__(self):
    return self.name
	
class singleID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getsingleid():
               try:
                        uuid = singleID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = singleID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               groupID = 'SIID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return groupID

class single_activity(models.Model):
  sid=models.CharField(default=getsingleid, max_length=200, unique=True)
  typeid=models.ForeignKey(single_activity_type, related_name="singleactivitytypeid", null= True)
  courseId=models.TextField(null=True,blank=True) 
  isActive=models.BooleanField(default=True)
  createdBy=models.ForeignKey(User, related_name="singleactivityCreatedBy", null= True)
  modifiedBy=models.ForeignKey(User, related_name="singleactivityModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  def __unicode__(self):
    return self.sid
	
class socialID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getsocialid():
               try:
                        uuid = socialID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = socialID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               groupID = 'SOID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return groupID

class social_activity(models.Model):
  soid=models.CharField(default=getsocialid, max_length=200, unique=True)
  noofsessions= models.IntegerField()
  courseId=models.TextField(null=True,blank=True) 
  isActive=models.BooleanField(default=True)
  createdBy=models.ForeignKey(User, related_name="socialactivityCreatedBy", null= True)
  modifiedBy=models.ForeignKey(User, related_name="socialactivityModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  def __unicode__(self):
    return self.soid
	
class topicweeklyID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def gettpicweeklyid():
               try:
                        uuid = topicweeklyID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = topicweeklyID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               groupID = 'TWID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return groupID	

class topics_weekly_activity(models.Model):
  twid=models.CharField(default=gettpicweeklyid, max_length=200, unique=True)
  noofsessions= models.IntegerField()
  courseId=models.TextField(null=True,blank=True) 
  showallsections=models.BooleanField(default=True)
  isActive=models.BooleanField(default=True)
  createdBy=models.ForeignKey(User, related_name="topicweklyactivityCreatedBy", null= True)
  modifiedBy=models.ForeignKey(User, related_name="topicweklyactivityModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  def __unicode__(self):
    return self.twid