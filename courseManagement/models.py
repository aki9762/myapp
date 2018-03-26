# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

#----------------------- Start parentCategory -------------------------#

class parCatUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getparentCategoryId():
               try:
                        uuid = parCatUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = parCatUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               parentCatID = 'parentCatID-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return parentCatID

class parentCategory(models.Model):
  courseCategoryId=models.CharField(default=getparentCategoryId, max_length=200, unique=True)
  parentCategoryId=models.TextField(null=True,blank=True)  
  categoryName=models.TextField(null=True,blank=True)
  description=models.TextField(null=True,blank=True)
  createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="parentCategoryCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="parentCategoryModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.categoryName

#----------------------- End parentCategory -------------------------#

#----------------------- Start filesUpload -------------------------#

class filesUploadUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getfilesUploadId():
               try:
                        uuid = filesUploadUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = filesUploadUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               filesUpload = 'fileUploadId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return filesUpload

class filesUpload(models.Model):
  fileUploadId=models.CharField(default=getfilesUploadId, max_length=200, unique=True)
  size=models.TextField(null=True,blank=True)  
  createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="filesUploadCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="filesUploadModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.size

#----------------------- End filesUpload -------------------------#

#----------------------- Start yesNo -------------------------#

class yesNoUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getyesNoId():
               try:
                        uuid = yesNoUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = yesNoUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               yesNoId = 'yesNoId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return yesNoId

class yesNo(models.Model):
  yesNoId=models.CharField(default=getyesNoId, max_length=200, unique=True)
  decision=models.TextField(null=True,blank=True)  
  createdBy= models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="yesNoCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="yesNoModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.decision

#----------------------- End yesNo -------------------------#


#----------------------- Start forceLanguage -------------------------#

class forceLanguageUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getforceLanguageId():
               try:
                        uuid = forceLanguageUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = forceLanguageUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               forceLangId = 'forceLangId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return forceLangId

class forceLanguage(models.Model):
  forceLangId=models.CharField(default=getforceLanguageId, max_length=200, unique=True)
  Language=models.TextField(null=True,blank=True)  
  createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="forceLanguageCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="forceLanguageModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.Language

#----------------------- End forceLanguage -------------------------#



#----------------------- Start courseLayout -------------------------#

class courseLayoutUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getcourseLayoutId():
               try:
                        uuid = courseLayoutUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = courseLayoutUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               courseLayoutId = 'courseLayoutId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return courseLayoutId

class courseLayout(models.Model):
  courseLayoutId=models.CharField(default=getcourseLayoutId, max_length=200, unique=True)
  courseLayoutDesc=models.TextField(null=True,blank=True)  
  createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="courseLayoutCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="courseLayoutModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.courseLayoutDesc

#----------------------- End courseLayout -------------------------#


#----------------------- Start hiddenSection -------------------------#


class hiddenSectionUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def gethiddenSectionId():
               try:
                        uuid = hiddenSectionUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = hiddenSectionUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               hiddenSectionId = 'hiddenSectionId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return hiddenSectionId

class hiddenSection(models.Model):
  hiddenSectionId=models.CharField(default=gethiddenSectionId, max_length=200, unique=True)
  hiddenSection=models.TextField(null=True,blank=True)  
  createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="hiddenSectionCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="hiddenSectionModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.hiddenSection

#----------------------- End hiddenSection -------------------------#



#----------------------- Start formattbl -------------------------#

class formatUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getformatId():
               try:
                        uuid = formatUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = formatUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               formatId = 'formatId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return formatId

class formattbl(models.Model):
  formatId=models.CharField(default=getformatId, max_length=200, unique=True)
  formatDes=models.TextField(null=True,blank=True)  
  createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatCreatedBy", null= True)
  modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatModifiedBy",null=True)
  createdDate=models.DateTimeField(auto_now_add=True)
  modifiedDate=models.DateTimeField(auto_now=True)
  isActive=models.BooleanField(default=True)
  def __unicode__(self):
    return self.formatDes

#----------------------- End formattbl -------------------------#


#----------------------- Start course -------------------------#

class courseUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getcourseId():
               try:
                        uuid = courseUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = courseUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               courseId = 'courseId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return courseId

class course(models.Model):
	courseId=models.CharField(default=getcourseId, max_length=200, unique=True)
	courseCategoryId=models.TextField(null=True,blank=True)  
	fullName=models.TextField(null=True,blank=True)  
	shortName=models.TextField(null=True,blank=True)  
	visibility=models.TextField(null=True,blank=True)  
	startDate=models.DateTimeField(null=True, blank=True)
	endDate=models.DateTimeField(null=True, blank=True)
	summary=models.TextField(null=True,blank=True)  
	formatId=models.TextField(null=True,blank=True)  
	numberOfSection=models.TextField(null=True,blank=True)  
	hiddenSectionId=models.TextField(null=True,blank=True)  
	courseLayoutId=models.TextField(null=True,blank=True)  
	forceLanguageID=models.TextField(null=True,blank=True)  
	numOfAnnounment=models.TextField(null=True,blank=True)  
	showGradesToStudent=models.TextField(null=True,blank=True)  
	showActivityReport=models.TextField(null=True,blank=True)  
	enableCompletionTracking=models.TextField(null=True,blank=True)  
	maxUploadSize=models.TextField(null=True,blank=True)  
	createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="courseCreatedBy", null= True)
	ModifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="courseModifiedBy",null=True)
	createdDate=models.DateTimeField(auto_now_add=True)
	modifiedDate=models.DateTimeField(auto_now=True)
	isActive=models.BooleanField(default=True)
def __unicode__(self):
	return self.course

#----------------------- End course -------------------------#




#----------------------- Start badges -------------------------#

class badgesUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getbadgesId():
               try:
                        uuid = badgesUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = badgesUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               badgesId = 'badgesId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return badgesId

class badges(models.Model):
	badgeId=models.CharField(default=getbadgesId, max_length=200, unique=True)
	badgeName=models.TextField(null=True,blank=True)  
	issuerName=models.TextField(null=True,blank=True)  
	issuerContact=models.TextField(null=True,blank=True)  
	description=models.TextField(null=True,blank=True)  
	expiryDate=models.DateTimeField(null=True, blank=True)
	createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatCreatedBy", null= True)
	modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatModifiedBy",null=True)
	createdDate=models.DateTimeField(auto_now_add=True)
	modifiedDate=models.DateTimeField(auto_now=True)
	isActive=models.BooleanField(default=True)
def __unicode__(self):
    return self.badgeName

#----------------------- End badges -------------------------#

#----------------------- Start competencyFramework -------------------------#

class competencyFrameworkUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def getcompetencyFrameworkId():
               try:
                        uuid = competencyFrameworkUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = competencyFrameworkUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               competencyFrameworkId = 'competencyId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return competencyFrameworkId

class competencyFramework(models.Model):
	compentencyId=models.CharField(default=getcompetencyFrameworkId, max_length=200, unique=True)
	competencyName=models.TextField(null=True,blank=True) 
	description=models.TextField(null=True,blank=True) 
	scale=models.TextField(null=True,blank=True) 
	visibile=models.TextField(null=True,blank=True) 
	category=models.TextField(null=True,blank=True) 
	level1=models.TextField(null=True,blank=True) 
	level2=models.TextField(null=True,blank=True) 
	level3=models.TextField(null=True,blank=True) 
	level4=models.TextField(null=True,blank=True) 
	createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatCreatedBy", null= True)
	modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatModifiedBy",null=True)
	createdDate=models.DateTimeField(auto_now_add=True)
	modifiedDate=models.DateTimeField(auto_now=True)
	isActive=models.BooleanField(default=True)
def __unicode__(self):
    return self.competencyName

#----------------------- End competencyFramework -------------------------#


#----------------------- Start taxonomies -------------------------#

class taxonomiesUUID(models.Model):
        uuidNumber = models.BigIntegerField(default=0)


# Function specifying custom id generation logic
def gettaxonomiesId():
               try:
                        uuid = taxonomiesUUID.objects.latest('uuidNumber')
               except Exception, e:
                        uuid = taxonomiesUUID()
                        
               uuid.uuidNumber = uuid.uuidNumber + 1
               taxonomiesId = 'taxonomiesId-'+ str(uuid.uuidNumber)
               uuid.save()
               
               return taxonomiesId

class taxonomies(models.Model):
	taxonomieId=models.CharField(default=gettaxonomiesId, max_length=200, unique=True)
	taxonomieName=models.TextField(null=True,blank=True) 
	createdBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatCreatedBy", null= True)
	modifiedBy=models.TextField(null=True,blank=True) #models.ForeignKey(User, related_name="formatModifiedBy",null=True)
	createdDate=models.DateTimeField(auto_now_add=True)
	modifiedDate=models.DateTimeField(auto_now=True)
	isActive=models.BooleanField(default=True)
def __unicode__(self):
    return self.taxonomieName

#----------------------- End taxonomies -------------------------#


class sample(models.Model):
  sampleName=models.TextField(null=True,blank=True)
def __unicode__(self):
    return self.sampleName 