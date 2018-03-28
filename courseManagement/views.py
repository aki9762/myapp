# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from django.shortcuts import render


from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


import json
#import requests
import datetime
import ast
from datetime import datetime
from django.core import serializers
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User,Group
from django.db import transaction
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import authenticate, login, logout

from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.utils import jwt_response_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
#importing the tables
from courseManagement.models import cohort,userCourses,subCategory,competencyFramework,parentCategory,filesUpload,yesNo,forceLanguage,courseLayout,hiddenSection,formattbl,course,taxonomies,badges # Load here the models that we are going to use while writing api's
from rest_framework.settings import api_settings
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView

from base64 import b64decode
# Create your views here. 

#---------------------------------- Start API's for Date conversion ----------------------------------------------------#
def getDatefromDateString(dateString):
    date = None    
    if(dateString != ""):
        date = datetime.strptime(dateString, "%d-%B-%Y").strftime("%Y-%m-%d")
        return date
    elif(dateString == 'undefined'):
        return date
    else:
        return date

def getDateStringfromDate(dateString):
    if(dateString == "" or dateString == None or dateString == "Null"):
        return ""
    else:
        date = dateString.strftime("%d-%B-%Y")
        return date
#----------------------------------  End of API's for Date conversion ----------------------------------------------------#

#---------------------------------- Start API's of  parentCategoryApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def parentCategoryApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['courseCategoryId'] == ""):
				parentCategoryDetail = parentCategory()
				#parentCategoryDetail.parentCategoryId = data["parentCategoryId"]
				parentCategoryDetail.categoryName = data["categoryName"]
				parentCategoryDetail.description = data["description"]
				parentCategoryDetail.createdBy_id = data["createdBy"]
				parentCategoryDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","courseCategoryId":parentCategoryDetail.courseCategoryId}),content_type="application/json")

			else:
				parentCategoryDetail = parentCategory.objects.get(courseCategoryId= data['courseCategoryId'])
				parentCategoryDetail.categoryName = data["categoryName"]
				parentCategoryDetail.description = data["description"]
				parentCategoryDetail.modifiedBy_id = data["modifiedBy"]
				parentCategoryDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","courseCategoryId":parentCategoryDetail.courseCategoryId}),content_type="application/json")
		
		if(data["action"] == "allList"):
			parentCatObj = parentCategory.objects.filter(isActive=True)
			parentCatList = []
			for sg in parentCatObj:
				obj = {"id":sg.id,"courseCategoryId":sg.courseCategoryId,"categoryName":sg.categoryName,"description":sg.description}
				parentCatList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","parentCatList":parentCatList}),content_type="application/json")

		if(data["action"] == "delete"):
			parentCategoryDetail = parentCategory.objects.get(courseCategoryId=data['courseCategoryId'])
			parentCategoryDetail.isActive=False
			parentCategoryDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

		elif(data["action"]=="list" or data["action"]=="search"):
			pageNo = data['pageNo']
			parentCatList=[]
			entriesPerPage = data['entriesPerPage']
			categoryName =data['categoryName']
			excludePageEntries = (pageNo - 1) * entriesPerPage
			nextPageEntries = excludePageEntries + entriesPerPage
			if(categoryName == ""):
				parentCategoryDetail = parentCategory.objects.filter(isActive=True).order_by('-id')[excludePageEntries:nextPageEntries]
				parCat_count = parentCategory.objects.filter(isActive=True).count()
				if(parCat_count>0):
					for sg in parentCategoryDetail:
						fam={"id":sg.id,"courseCategoryId":sg.courseCategoryId,"categoryName":sg.categoryName,"description":sg.description}
						parentCatList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","parentCategoryDetail":parentCatList,"parCat_count":parCat_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","parentCategoryDetail":parentCatList,"parCat_count":0,"pageNo":1}), content_type="application/json")
			elif(categoryName!=""):
				parentCategoryDetail = parentCategory.objects.filter(isActive=True).filter(categoryName__icontains=data["categoryName"]).order_by('-id')[excludePageEntries:nextPageEntries]
				parCat_count = parentCategory.objects.filter(isActive=True).filter(categoryName__icontains=data["categoryName"]).count()
				if(parCat_count>0):
					for sg in parentCategoryDetail:
						fam={"id":sg.id,"courseCategoryId":sg.courseCategoryId,"categoryName":sg.categoryName,"description":sg.description}
						parentCatList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","parentCategoryDetail":parentCatList,"parCat_count":parCat_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","parentCategoryDetail":parentCatList,"parCat_count":0,"pageNo":1}), content_type="application/json")           
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce_code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of parentCategoryApi ------------------------------------------------------#

#---------------------------------- Start API's of  getfileUplaod ----------------------------------------------------#
@api_view(['GET'])
def getfileUplaod(request):
    try:
        filesUploadList=[]
        filesUploadDetails=filesUpload.objects.filter(isActive=True)
        for fu in filesUploadDetails:
            obj={"id":fu.id,"fileUploadId":fu.fileUploadId,"size":fu.size}   
            filesUploadList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","filesUploadList":filesUploadList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of getfileUplaod ------------------------------------------------------#

#---------------------------------- Start API's of  getyesNo ----------------------------------------------------#
@api_view(['GET'])
def getyesNo(request):
    try:
        yesNoList=[]
        yesNoDetails=yesNo.objects.filter(isActive=True)
        for fu in yesNoDetails:
            obj={"id":fu.id,"yesNoId":fu.yesNoId,"decision":fu.decision}
            yesNoList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","yesNoList":yesNoList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of getyesNo ------------------------------------------------------#


#---------------------------------- Start API's of  getforceLanguage ----------------------------------------------------#
@api_view(['GET'])
def getforceLanguage(request):
    try:
        forceLanguageList=[]
        forceLanguageDetails=forceLanguage.objects.filter(isActive=True)
        for fu in forceLanguageDetails:
            obj={"id":fu.id,"forceLangId":fu.forceLangId,"Language":fu.Language}
            forceLanguageList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","forceLanguageList":forceLanguageList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of getforceLanguage ------------------------------------------------------#


#---------------------------------- Start API's of  getcourseLayout ----------------------------------------------------#
@api_view(['GET'])
def getcourseLayout(request):
    try:
        courseLayoutList=[]
        courseLayoutDetails=courseLayout.objects.filter(isActive=True)
        for fu in courseLayoutDetails:
            obj={"id":fu.id,"courseLayoutId":fu.courseLayoutId,"courseLayoutDesc":fu.courseLayoutDesc}
            courseLayoutList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","courseLayoutList":courseLayoutList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of getforceLanguage ------------------------------------------------------#

#---------------------------------- Start API's of  gethiddenSection ----------------------------------------------------#
@api_view(['GET'])
def gethiddenSection(request):
    try:
        hiddenSectionLayoutList=[]
        hiddenSectionDetails=hiddenSection.objects.filter(isActive=True)
        for fu in hiddenSectionDetails:
            obj={"id":fu.id,"hiddenSectionId":fu.hiddenSectionId,"hiddenSection":fu.hiddenSection}
            hiddenSectionLayoutList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","hiddenSectionLayoutList":hiddenSectionLayoutList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of getforceLanguage ------------------------------------------------------#

#---------------------------------- Start API's of  getformattbl ----------------------------------------------------#
@api_view(['GET'])
def getformattbl(request):
    try:
        formattblLayoutList=[]
        formattblDetails=formattbl.objects.filter(isActive=True)
        for fu in formattblDetails:
            obj={"id":fu.id,"formatId":fu.formatId,"formatDes":fu.formatDes}
            formattblLayoutList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","formattblLayoutList":formattblLayoutList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of getforceLanguage ------------------------------------------------------#




#---------------------------------- Start API's of  courseApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def courseApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['courseId'] == ""):
				courseDetail = course()				
				courseDetail.courseCategoryId = data["courseCategoryId"]
				courseDetail.fullName = data["fullName"]				
				courseDetail.shortName = data["shortName"]
				courseDetail.visibility= data["visibility"]
				courseDetail.startDate = getDatefromDateString(data["startDate"])
				courseDetail.endDate = getDatefromDateString(data["endDate"])
				courseDetail.summary = data["summary"]				
				courseDetail.formatId = data["formatId"]
				courseDetail.numberOfSection = data["numberOfSection"]				
				courseDetail.hiddenSectionId = data["hiddenSectionId"]
				courseDetail.courseLayoutId = data["courseLayoutId"]
				courseDetail.forceLanguageID = data["forceLanguageID"]
				courseDetail.numOfAnnounment = data["numOfAnnounment"]
				courseDetail.showGradesToStudent = data["showGradesToStudent"]
				courseDetail.showActivityReport = data["showActivityReport"]
				courseDetail.enableCompletionTracking = data["enableCompletionTracking"]
				courseDetail.maxUploadSize = data["maxUploadSize"]
				courseDetail.createdBy_id = data["createdBy"]
				courseDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","courseId":courseDetail.courseId}),content_type="application/json")

			else:
				courseDetail = course.objects.get(courseId= data['courseId'])
				courseDetail.courseCategoryId = data["courseCategoryId"]
				courseDetail.fullName = data["fullName"]				
				courseDetail.shortName = data["shortName"]
				courseDetail.visibility= data["visibility"]
				courseDetail.startDate = getDatefromDateString(data["startDate"])
				courseDetail.endDate = getDatefromDateString(data["endDate"])
				courseDetail.summary = data["summary"]				
				courseDetail.formatId = data["formatId"]
				courseDetail.numberOfSection = data["numberOfSection"]				
				courseDetail.hiddenSectionId = data["hiddenSectionId"]
				courseDetail.courseLayoutId = data["courseLayoutId"]
				courseDetail.forceLanguageID = data["forceLanguageID"]
				courseDetail.numOfAnnounment = data["numOfAnnounment"]
				courseDetail.showGradesToStudent = data["showGradesToStudent"]
				courseDetail.showActivityReport = data["showActivityReport"]
				courseDetail.enableCompletionTracking = data["enableCompletionTracking"]
				courseDetail.maxUploadSize = data["maxUploadSize"]
				courseDetail.modifiedBy_id = data["modifiedBy"]
				courseDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","courseId":courseDetail.courseId}),content_type="application/json")
		
		if(data["action"] == "allList"):
			courseObj = course.objects.filter(isActive=True)
			courseList = []
			for sg in courseObj:
				obj = {"id":sg.id,
						"courseId":sg.courseId,
						"courseCategoryId":sg.courseCategoryId,
						"fullName":sg.fullName,
						"shortName":sg.shortName,	
						"visibility":sg.visibility,
						"startDate":getDateStringfromDate(sg.startDate),
						"endDate":getDateStringfromDate(sg.endDate),
						"summary":sg.summary,
						"formatId":sg.formatId,
						"numberOfSection":sg.numberOfSection,
						"hiddenSectionId":sg.hiddenSectionId,
						"courseLayoutId":sg.courseLayoutId,
						"forceLanguageID":sg.forceLanguageID,
						"numOfAnnounment":sg.numOfAnnounment,
						"showGradesToStudent":sg.showGradesToStudent,
						"showActivityReport":sg.showActivityReport,
						"enableCompletionTracking":sg.enableCompletionTracking,
						"maxUploadSize":sg.maxUploadSize
						}
				courseList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","courseList":courseList}),content_type="application/json")

		if(data["action"] == "delete"):
			courseDetail = course.objects.get(courseId=data['courseId'])
			courseDetail.isActive=False
			courseDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")
		if(data["action"]=="list" or data["action"]=="search"):
			pageNo = data['pageNo']
			courseList=[]
			entriesPerPage = data['entriesPerPage']
			fullName =data['fullName']
			excludePageEntries = (pageNo - 1) * entriesPerPage
			nextPageEntries = excludePageEntries + entriesPerPage
			if(fullName == ""):
				courseDetail = course.objects.filter(isActive=True).order_by('-id')[excludePageEntries:nextPageEntries]
				course_count = course.objects.filter(isActive=True).count()
				if(course_count>0):
					for sg in courseDetail:
						fam= {"id":sg.id,
						"courseId":sg.courseId,
						"courseCategoryId":sg.courseCategoryId,
						"fullName":sg.fullName,
						"shortName":sg.shortName,	
						"visibility":sg.visibility,
						"startDate":getDateStringfromDate(sg.startDate),
						"endDate":getDateStringfromDate(sg.endDate),
						"summary":sg.summary,
						"formatId":sg.formatId,
						"numberOfSection":sg.numberOfSection,
						"hiddenSectionId":sg.hiddenSectionId,
						"courseLayoutId":sg.courseLayoutId,
						"forceLanguageID":sg.forceLanguageID,
						"numOfAnnounment":sg.numOfAnnounment,
						"showGradesToStudent":sg.showGradesToStudent,
						"showActivityReport":sg.showActivityReport,
						"enableCompletionTracking":sg.enableCompletionTracking,
						"maxUploadSize":sg.maxUploadSize
						}
						courseList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","courseDetail":courseList,"course_count":course_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","courseDetail":courseList,"course_count":0,"pageNo":1}), content_type="application/json")
			elif(fullName!=""):
				courseDetail = course.objects.filter(isActive=True).filter(fullName__icontains=data["fullName"]).order_by('-id')[excludePageEntries:nextPageEntries]
				course_count = course.objects.filter(isActive=True).filter(fullName__icontains=data["fullName"]).count()
				if(course_count>0):
					for sg in courseDetail:
						fam= {"id":sg.id,
						"courseId":sg.courseId,
						"courseCategoryId":sg.courseCategoryId,
						"fullName":sg.fullName,
						"shortName":sg.shortName,	
						"visibility":sg.visibility,
						"startDate":getDateStringfromDate(sg.startDate),
						"endDate":getDateStringfromDate(sg.endDate),
						"summary":sg.summary,
						"formatId":sg.formatId,
						"numberOfSection":sg.numberOfSection,
						"hiddenSectionId":sg.hiddenSectionId,
						"courseLayoutId":sg.courseLayoutId,
						"forceLanguageID":sg.forceLanguageID,
						"numOfAnnounment":sg.numOfAnnounment,
						"showGradesToStudent":sg.showGradesToStudent,
						"showActivityReport":sg.showActivityReport,
						"enableCompletionTracking":sg.enableCompletionTracking,
						"maxUploadSize":sg.maxUploadSize
						}
						courseList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","courseDetail":courseList,"course_count":course_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","courseDetail":courseList,"course_count":0,"pageNo":1}), content_type="application/json")  
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of courseApi ------------------------------------------------------#

#---------------------------------- Start API's of  taxonomies ----------------------------------------------------#
@api_view(['GET'])
def gettaxonomies(request):
    try:
        taxonomiesList=[]
        taxonomiesDetails=taxonomies.objects.filter(isActive=True)
        for fu in taxonomiesDetails:
            obj={"id":fu.id,"taxonomieId":fu.taxonomieId,"taxonomieName":fu.taxonomieName}
            taxonomiesList.append(obj)
        return HttpResponse(json.dumps({"response_code":200,"Status":"Success","taxonomiesList":taxonomiesList}),content_type="application/json")
    except Exception as e:
        error=str(e)
        return HttpResponse(json.dumps({"response_code":500,"Status":"Failed","error":error}),content_type="application/json")
#---------------------------------- End API's of taxonomies ------------------------------------------------------#



#---------------------------------- Start API's of  badgesApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def badgesApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['badgeId'] == ""):
				badgesDetail = badges()	
				badgesDetail.badgeName= data["badgeName"]	
				badgesDetail.issuerName= data["issuerName"]	
				badgesDetail.issuerContact= data["issuerContact"]	
				badgesDetail.description= data["description"]	
				badgesDetail.expiryDate= getDatefromDateString(data["expiryDate"])		
				badgesDetail.createdBy_id = data["createdBy"]
				badgesDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","badgeId":badgesDetail.badgeId}),content_type="application/json")

			else:
				badgesDetail = badges.objects.get(badgeId= data['badgeId'])
				badgesDetail.badgeName= data["badgeName"]	
				badgesDetail.issuerName= data["issuerName"]	
				badgesDetail.issuerContact= data["issuerContact"]	
				badgesDetail.description= data["description"]	
				badgesDetail.expiryDate= getDatefromDateString(data["expiryDate"])		
				badgesDetail.modifiedBy_id = data["modifiedBy"]
				badgesDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","badgeId":badgesDetail.badgeId}),content_type="application/json")
		
		if(data["action"] == "allList"):
			badgesObj = badges.objects.filter(isActive=True)
			badgesList = []
			for sg in badgesObj:
				obj = {"id":sg.id,
						"badgeId":sg.badgeId,
						"badgeName":sg.badgeName,
						"issuerName":sg.issuerName,
						"issuerContact":sg.issuerContact,	
						"description":sg.description,
						"expiryDate":getDateStringfromDate(sg.expiryDate)
						}
				badgesList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","badgesList":badgesList}),content_type="application/json")

		if(data["action"] == "delete"):
			badgesDetail = badges.objects.get(badgeId=data['badgeId'])
			badgesDetail.isActive=False
			badgesDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")
		if(data["action"]=="list" or data["action"]=="search"):
			pageNo = data['pageNo']
			badgesList=[]
			entriesPerPage = data['entriesPerPage']
			badgeName =data['badgeName']
			excludePageEntries = (pageNo - 1) * entriesPerPage
			nextPageEntries = excludePageEntries + entriesPerPage
			if(badgeName == ""):
				badgesDetail = badges.objects.filter(isActive=True).order_by('-id')[excludePageEntries:nextPageEntries]
				badges_count = badges.objects.filter(isActive=True).count()
				if(badges_count>0):
					for sg in badgesDetail:
						fam=  {"id":sg.id,
						"badgeId":sg.badgeId,
						"badgeName":sg.badgeName,
						"issuerName":sg.issuerName,
						"issuerContact":sg.issuerContact,	
						"description":sg.description,
						"expiryDate":getDateStringfromDate(sg.expiryDate)
						}
						badgesList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","badgesDetail":badgesList,"badges_count":badges_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","badgesDetail":badgesList,"badges_count":0,"pageNo":1}), content_type="application/json")
			elif(badgeName!=""):
				badgesDetail = badges.objects.filter(isActive=True).filter(badgeName__icontains=data["badgeName"]).order_by('-id')[excludePageEntries:nextPageEntries]
				badges_count = badges.objects.filter(isActive=True).filter(badgeName__icontains=data["badgeName"]).count()
				if(badges_count>0):
					for sg in badgesDetail:
						fam=  {"id":sg.id,
						"badgeId":sg.badgeId,
						"badgeName":sg.badgeName,
						"issuerName":sg.issuerName,
						"issuerContact":sg.issuerContact,	
						"description":sg.description,
						"expiryDate":getDateStringfromDate(sg.expiryDate)
						}
						badgesList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","badgesDetail":badgesList,"badges_count":badges_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","badgesDetail":badgesList,"badges_count":0,"pageNo":1}), content_type="application/json")  
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of badgesApi ------------------------------------------------------#


#---------------------------------- Start API's of  competencyFrameworkApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def competencyFrameworkApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['compentencyId'] == ""):
				competencyFrameworkDetail = competencyFramework()	
				competencyFrameworkDetail.competencyName= data["competencyName"]
				competencyFrameworkDetail.description= data["description"]
				competencyFrameworkDetail.scale= data["scale"]
				competencyFrameworkDetail.visibile= data["visibile"]
				competencyFrameworkDetail.category= data["category"]
				competencyFrameworkDetail.level1= data["level1"]
				competencyFrameworkDetail.level2= data["level2"]
				competencyFrameworkDetail.level3= data["level3"]
				competencyFrameworkDetail.level4= data["level4"]	
				competencyFrameworkDetail.createdBy_id = data["createdBy"]
				competencyFrameworkDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","compentencyId":competencyFrameworkDetail.compentencyId}),content_type="application/json")

			else:
				competencyFrameworkDetail = competencyFramework.objects.get(compentencyId= data['compentencyId'])
		
				competencyFrameworkDetail.competencyName= data["competencyName"]
				competencyFrameworkDetail.description= data["description"]
				competencyFrameworkDetail.scale= data["scale"]
				competencyFrameworkDetail.visibile= data["visibile"]
				competencyFrameworkDetail.category= data["category"]
				competencyFrameworkDetail.level1= data["level1"]
				competencyFrameworkDetail.level2= data["level2"]
				competencyFrameworkDetail.level3= data["level3"]
				competencyFrameworkDetail.level4= data["level4"]	
				competencyFrameworkDetail.modifiedBy_id = data["modifiedBy"]
				competencyFrameworkDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","compentencyId":competencyFrameworkDetail.compentencyId}),content_type="application/json")
		
		if(data["action"] == "allList"):
			competencyFrameworkObj = competencyFramework.objects.filter(isActive=True)
			competencyFrameworkList = []
			for sg in competencyFrameworkObj:
				obj = {"id":sg.id,
						"compentencyId":sg.compentencyId,
						"competencyName":sg.competencyName,
						"description":sg.description,
						"scale":sg.scale,	
						"visibile":sg.visibile,
						"category":sg.category,
						"level1":sg.level1,
						"level2":sg.level2,
						"level3":sg.level3,
						"level4":sg.level4
						}
				competencyFrameworkList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","competencyFrameworkList":competencyFrameworkList}),content_type="application/json")

		if(data["action"] == "delete"):
			competencyFrameworkDetail = competencyFramework.objects.get(compentencyId=data['compentencyId'])
			competencyFrameworkDetail.isActive=False
			competencyFrameworkDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")
		if(data["action"]=="list" or data["action"]=="search"):
			pageNo = data['pageNo']
			competencyFrameworkList=[]
			entriesPerPage = data['entriesPerPage']
			competencyName =data['competencyName']
			excludePageEntries = (pageNo - 1) * entriesPerPage
			nextPageEntries = excludePageEntries + entriesPerPage
			if(competencyName == ""):
				competencyFrameworkDetail = competencyFramework.objects.filter(isActive=True).order_by('-id')[excludePageEntries:nextPageEntries]
				competencyFramework_count = competencyFramework.objects.filter(isActive=True).count()
				if(competencyFramework_count>0):
					for sg in competencyFrameworkDetail:
						fam=  {"id":sg.id,
						"compentencyId":sg.compentencyId,
						"competencyName":sg.competencyName,
						"description":sg.description,
						"scale":sg.scale,	
						"visibile":sg.visibile,
						"category":sg.category,
						"level1":sg.level1,
						"level2":sg.level2,
						"level3":sg.level3,
						"level4":sg.level4
						}
						competencyFrameworkList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","competencyFrameworkDetail":competencyFrameworkList,"competencyFramework_count":competencyFramework_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","competencyFrameworkDetail":competencyFrameworkList,"competencyFramework_count":0,"pageNo":1}), content_type="application/json")
			elif(competencyName!=""):
				competencyFrameworkDetail = competencyFramework.objects.filter(isActive=True).filter(competencyName__icontains=data["competencyName"]).order_by('-id')[excludePageEntries:nextPageEntries]
				competencyFramework_count = competencyFramework.objects.filter(isActive=True).filter(competencyName__icontains=data["competencyName"]).count()
				if(competencyFramework_count>0):
					for sg in competencyFrameworkDetail:
						fam=  {"id":sg.id,
						"compentencyId":sg.compentencyId,
						"competencyName":sg.competencyName,
						"description":sg.description,
						"scale":sg.scale,	
						"visibile":sg.visibile,
						"category":sg.category,
						"level1":sg.level1,
						"level2":sg.level2,
						"level3":sg.level3,
						"level4":sg.level4
						}
						competencyFrameworkList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","competencyFrameworkDetail":competencyFrameworkList,"competencyFramework_count":competencyFramework_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","competencyFrameworkDetail":competencyFrameworkList,"competencyFramework_count":0,"pageNo":1}), content_type="application/json")  
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of competencyFrameworkApi ------------------------------------------------------#

#---------------------------------- Start API's of  subCategoryApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def subCategoryApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['subCategoryId'] == ""):
				subCategoryDetail = subCategory()				
				subCategoryDetail.parentCategoryId = data["parentCategoryId"]
				subCategoryDetail.subCategoryName = data["subCategoryName"]
				subCategoryDetail.description = data["description"]
				subCategoryDetail.createdBy_id = data["createdBy"]
				subCategoryDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","subCategoryId":subCategoryDetail.subCategoryId}),content_type="application/json")

			else:
				subCategoryDetail = subCategory.objects.get(subCategoryId= data['subCategoryId'])
				subCategoryDetail.parentCategoryId = data["parentCategoryId"]
				subCategoryDetail.subCategoryName = data["subCategoryName"]
				subCategoryDetail.description = data["description"]
				subCategoryDetail.modifiedBy_id = data["modifiedBy"]
				subCategoryDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","subCategoryId":subCategoryDetail.subCategoryId}),content_type="application/json")
		
		if(data["action"] == "allList"):
			subCatObj = subCategory.objects.filter(isActive=True)
			subCatList = []
			for sg in subCatObj:
				obj = {"id":sg.id,"subCategoryId":sg.subCategoryId,"parentCategoryId":sg.parentCategoryId,"subCategoryName":sg.subCategoryName,"description":sg.description}
				subCatList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","subCatList":subCatList}),content_type="application/json")

		if(data["action"] == "delete"):
			subCategoryDetail = subCategory.objects.get(subCategoryId=data['subCategoryId'])
			subCategoryDetail.isActive=False
			subCategoryDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

		elif(data["action"]=="list" or data["action"]=="search"):
			pageNo = data['pageNo']
			subCatList=[]
			entriesPerPage = data['entriesPerPage']
			subCategoryName =data['subCategoryName']
			excludePageEntries = (pageNo - 1) * entriesPerPage
			nextPageEntries = excludePageEntries + entriesPerPage
			if(subCategoryName == ""):
				subCategoryDetail = subCategory.objects.filter(isActive=True).order_by('-id')[excludePageEntries:nextPageEntries]
				subCat_count = subCategory.objects.filter(isActive=True).count()
				if(subCat_count>0):
					for sg in subCategoryDetail:
						fam={"id":sg.id,"subCategoryId":sg.subCategoryId,"parentCategoryId":sg.parentCategoryId,"subCategoryName":subCategoryName,"description":sg.description}
						subCatList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","subCategoryDetail":subCatList,"subCat_count":subCat_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","subCategoryDetail":subCatList,"subCat_count":0,"pageNo":1}), content_type="application/json")
			elif(subCategoryName!=""):
				subCategoryDetail = subCategory.objects.filter(isActive=True).filter(subCategoryName__icontains=data["subCategoryName"]).order_by('-id')[excludePageEntries:nextPageEntries]
				subCat_count = subCategory.objects.filter(isActive=True).filter(subCategoryName__icontains=data["subCategoryName"]).count()
				if(subCat_count>0):
					for sg in subCategoryDetail:
						fam={"id":sg.id,"subCategoryId":sg.subCategoryId,"parentCategoryId":sg.parentCategoryId,"subCategoryName":subCategoryName,"description":sg.description}
						subCatList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","subCategoryDetail":subCatList,"subCat_count":subCat_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","subCategoryDetail":subCatList,"subCat_count":0,"pageNo":1}), content_type="application/json")           
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce_code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of subCategoryApi ---.---------------------------------------------------#


#---------------------------------- Start API's of  userCoursesApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def userCoursesApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['userCourseId'] == ""):
				userCoursesDetail = userCourses()				
				userCoursesDetail.userId = data["userId"]
				userCoursesDetail.courseId = data["courseId"]
				userCoursesDetail.completionFlag = data["completionFlag"]
				userCoursesDetail.createdBy_id = data["createdBy"]
				userCoursesDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","userCourseId":userCoursesDetail.userCourseId}),content_type="application/json")


			else:
				userCoursesDetail = userCourses.objects.get(userCourseId= data['userCourseId'])
				userCoursesDetail.userId = data["userId"]
				userCoursesDetail.courseId = data["courseId"]
				userCoursesDetail.completionFlag = data["completionFlag"]
				userCoursesDetail.modifiedBy_id = data["modifiedBy"]
				userCoursesDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","userCourseId":userCoursesDetail.userCourseId}),content_type="application/json")
		
		if(data["action"] == "allList"):
			userCoursesObj = userCourses.objects.filter(isActive=True)
			userCoursesList = []
			for sg in userCoursesObj:
				obj = {"id":sg.id,"userCourseId":sg.userCourseId,"userId":sg.userId,"courseId":sg.courseId,"completionFlag":sg.completionFlag}
				userCoursesList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","userCoursesList":userCoursesList}),content_type="application/json")

		if(data["action"] == "delete"):
			userCoursesDetail = userCourses.objects.get(userCourseId=data['userCourseId'])
			userCoursesDetail.isActive=False
			userCoursesDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")
		if(data["action"] == "update"):
			userCoursesDetail = userCourses.objects.get(userCourseId=data['userCourseId'])
			if(data['check']=="1"):
				userCoursesDetail.completionFlag="1"
			else:
				userCoursesDetail.completionFlag="0"
			userCoursesDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","userCourseId":userCoursesDetail.userCourseId}),content_type="application/json")
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce_code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of userCoursesApi ---.---------------------------------------------------#

#---------------------------------- Start API's of customFileUploadAPI ---.---------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def customFileUploadAPI(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['id'] == ""):
				customFileUploadDetail = customFileUpload()	
				customFileUploadDetail.custom1=data['custom1']
				customFileUploadDetail.custom2=data['custom2']
				customFileUploadDetail.custom3=data['custom3']
				customFileUploadDetail.custom4=data['custom4']
				customFileUploadDetail.custom5=data['custom5']
				customFileUploadDetail.fileToUpload=data['fileToUpload']	
				customFileUploadDetail.createdBy_id = data["createdBy"]
				customFileUploadDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","customFileUploadId":customFileUpload.id}),content_type="application/json")
			else:
				customFileUploadDetail = customFileUpload.objects.get(id= data['id'])
				customFileUploadDetail.custom1=data['custom1']
				customFileUploadDetail.custom2=data['custom2']
				customFileUploadDetail.custom3=data['custom3']
				customFileUploadDetail.custom4=data['custom4']
				customFileUploadDetail.custom5=data['custom5']
				#customFileUploadDetail.fileToUpload=data['fileToUpload']
				if(data["fileToUpload"]==None or data["fileToUpload"]=="" or data["fileToUpload"]=="Null"):
					pass
				else:
					customFileUploadDetail.fileToUpload=data["fileToUpload"]		
				customFileUploadDetail.modifiedBy_id = data["modifiedBy"]
				customFileUploadDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","customFileUploadId":customFileUpload.id}),content_type="application/json")
		
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce_code":"500","error":str(e) }), content_type="application/json")
#---------------------------------- End API's of customFileUploadAPI ---.---------------------------------------------------#

#---------------------------------- Start API's of  cohortApi ----------------------------------------------------#

@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def cohortApi(request):
	try:
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['cohortId'] == ""):
				cohortDetail.cohortDetail = cohort()		
				cohortDetail.context= data["context"]
				cohortDetail.cohortName= data["cohortName"]
				cohortDetail.visibility= data["visibility"]
				cohortDetail.description= data["description"]		
				cohortDetail.createdBy_id = data["createdBy"]
				cohortDetail.save()
				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","cohortId":cohortDetail.cohortId}),content_type="application/json")
			else:
				cohortDetail = cohort.objects.get(cohortId= data['cohortId'])
				cohortDetail.context= data["context"]
				cohortDetail.cohortName= data["cohortName"]
				cohortDetail.visibility= data["visibility"]
				cohortDetail.description= data["description"]		
				cohortDetail.modifiedBy_id = data["modifiedBy"]
				cohortDetail.save()
				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","cohortId":cohortDetail.cohortId}),content_type="application/json")
		if(data["action"] == "allList"):
			cohortObj = cohort.objects.filter(isActive=True)
			cohortList = []
			for sg in cohortObj:
				obj = {"id":sg.id,"cohortId":sg.cohortId,"context":sg.context,"cohortName":sg.cohortName,"visibility":sg.visibility,"description":sg.description}
				cohortList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","cohortList":cohortList}),content_type="application/json")

		if(data["action"] == "delete"):
			cohortDetail = cohort.objects.get(cohortId=data['cohortId'])
			cohortDetail.isActive=False
			cohortDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")
		elif(data["action"]=="list" or data["action"]=="search"):
			pageNo = data['pageNo']
			cohortList=[]
			entriesPerPage = data['entriesPerPage']
			cohortName =data['cohortName']
			excludePageEntries = (pageNo - 1) * entriesPerPage
			nextPageEntries = excludePageEntries + entriesPerPage
			if(cohortName == ""):
				cohortDetail = cohort.objects.filter(isActive=True).order_by('-id')[excludePageEntries:nextPageEntries]
				cohort_count = cohort.objects.filter(isActive=True).count()
				if(cohort_count>0):
					for sg in cohortDetail:
						fam={"id":sg.id,"cohortId":sg.cohortId,"context":sg.context,"cohortName":sg.cohortName,"visibility":sg.visibility,"description":sg.description}
						cohortList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","cohortDetail":cohortList,"cohort_count":cohort_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","cohortDetail":cohortList,"cohort_count":0,"pageNo":1}), content_type="application/json")
			elif(cohortName!=""):
				cohortDetail = cohort.objects.filter(isActive=True).filter(cohortName__icontains=data["cohortName"]).order_by('-id')[excludePageEntries:nextPageEntries]
				cohort_count = cohort.objects.filter(isActive=True).filter(cohortName__icontains=data["cohortName"]).count()
				if(cohort_count>0):
					for sg in cohortDetail:
						fam={"id":sg.id,"cohortId":sg.cohortId,"context":sg.context,"cohortName":sg.cohortName,"visibility":sg.visibility,"description":sg.description}
						cohortList.append(fam)
					return HttpResponse(json.dumps({"response code":"200","status": "Success","cohortDetail":cohortList,"cohort_count":cohort_count,"pageNo":pageNo}), content_type="application/json")
				else:
					return HttpResponse(json.dumps({"response code":"300","status": "Success","cohortDetail":cohortList,"cohort_count":0,"pageNo":1}), content_type="application/json")
	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce_code":"500","error":str(e) }), content_type="application/json")


#---------------------------------- End API's of userCoursesApi ---.---------------------------------------------------#
