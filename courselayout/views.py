# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
#import requests
import datetime
import ast

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from courselayout.models import format_type, single_activity_type, single_activity, social_activity, topics_weekly_activity

# Create your views here.

@api_view(['GET'])				
def createsuperuser(request):	
			user=User.objects.create_user('admin1', password='Demo@123')
			user.is_superuser=True
			user.is_staff=True
			user.save()
			return HttpResponse(json.dumps({"responce code":"100","status": "success" ,"user" : user.id}), content_type="application/json")
			
@api_view(['GET'])			
def getcourseformats(request):	
			cformat= format_type.objects.filter(isActive = "1")
			courseformat = []
			for sg in cformat:
				obj = {"id":sg.id,"name":sg.name}
				courseformat.append(obj)
			return HttpResponse(json.dumps({"responce code":"100","status": "success" ,"courseformat" : courseformat}), content_type="application/json")
			
@api_view(['POST'])
def singleactivitytype(request):
	try:
		# return HttpResponse(json.dumps({"responsecode":id}))
		
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['Actid'] == ""):
				subjectGroupDetail = single_activity_type()
				subjectGroupDetail.name = data["name"]
				user = User.objects.get(id= data["createdBy"])
				subjectGroupDetail.createdBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","Actid":subjectGroupDetail.actid}),content_type="application/json")

			else:
				subjectGroupDetail = single_activity_type.objects.get(actid= data['Actid'])
				subjectGroupDetail.name = data["name"]
				user = User.objects.get(id= data["modifiedBy"])
				subjectGroupDetail.modifiedBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","Actid":subjectGroupDetail.actid}),content_type="application/json")
		
		if(data["action"] == "allList"):
			subjectGroupObj = single_activity_type.objects.filter(isActive=True)
			subjectGroupList = []
			for sg in subjectGroupObj:
				obj = {"id":sg.id,"Actid":sg.actid,"name":sg.name}
				subjectGroupList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","data":subjectGroupList}),content_type="application/json")

		if(data["action"] == "delete"):
			subjectGroupDetail = single_activity_type.objects.get(Actid=data['Actid'])
			subjectGroupDetail.isActive=False
			subjectGroupDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")

@api_view(['POST'])
def singleactivity(request):
	try:
		# return HttpResponse(json.dumps({"responsecode":id}))
		
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['sid'] == ""):
				subjectGroupDetail = single_activity()
				type = single_activity_type.objects.get(id= data["typeid"])
				subjectGroupDetail.typeid = type
				subjectGroupDetail.courseId = data["courseId"]
				user = User.objects.get(id= data["createdBy"])
				subjectGroupDetail.createdBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","sid":subjectGroupDetail.sid}),content_type="application/json")

			else:
				subjectGroupDetail = single_activity.objects.get(sid= data['sid'])
				type = single_activity_type.objects.get(id= data["typeid"])
				subjectGroupDetail.typeid = type
				subjectGroupDetail.courseId = data["courseId"]
				user = User.objects.get(id= data["modifiedBy"])
				subjectGroupDetail.modifiedBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","sid":subjectGroupDetail.sid}),content_type="application/json")
		
		if(data["action"] == "allList"):
			subjectGroupObj = single_activity.objects.filter(isActive=True)
			subjectGroupList = []
			for sg in subjectGroupObj:
				obj = {"id":sg.id,"sid":sg.sid,"typeid": sg.typeid.id,"courseId":sg.courseId}
				subjectGroupList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","data":subjectGroupList}),content_type="application/json")

		if(data["action"] == "delete"):
			subjectGroupDetail = single_activity.objects.get(sid=data['sid'])
			subjectGroupDetail.isActive=False
			subjectGroupDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")
		
@api_view(['POST'])
def socialactivity(request):
	try:
		# return HttpResponse(json.dumps({"responsecode":id}))
		
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['soid'] == ""):
				subjectGroupDetail = social_activity()
				subjectGroupDetail.noofsessions = data["noofsessions"]
				subjectGroupDetail.courseId = data["courseId"]
				user = User.objects.get(id= data["createdBy"])
				subjectGroupDetail.createdBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","soid":subjectGroupDetail.soid}),content_type="application/json")

			else:
				subjectGroupDetail = social_activity.objects.get(soid= data['soid'])
				subjectGroupDetail.noofsessions = data["noofsessions"]
				subjectGroupDetail.courseId = data["courseId"]
				user = User.objects.get(id= data["modifiedBy"])
				subjectGroupDetail.modifiedBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","soid":subjectGroupDetail.soid}),content_type="application/json")
		
		if(data["action"] == "allList"):
			subjectGroupObj = social_activity.objects.filter(isActive=True)
			subjectGroupList = []
			for sg in subjectGroupObj:
				obj = {"id":sg.id,"soid":sg.soid,"noofsessions": sg.noofsessions,"courseId":sg.courseId}
				subjectGroupList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","data":subjectGroupList}),content_type="application/json")

		if(data["action"] == "delete"):
			subjectGroupDetail = social_activity.objects.get(soid=data['soid'])
			subjectGroupDetail.isActive=False
			subjectGroupDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")
		
@api_view(['POST'])
def topicweeklyactivity(request):
	try:
		# return HttpResponse(json.dumps({"responsecode":id}))
		
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['twid'] == ""):
				subjectGroupDetail = topics_weekly_activity()
				subjectGroupDetail.noofsessions = data["noofsessions"]
				subjectGroupDetail.courseId = data["courseId"]
				subjectGroupDetail.showallsections = data["showallsections"]
				user = User.objects.get(id= data["createdBy"])
				subjectGroupDetail.createdBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","twid":subjectGroupDetail.twid}),content_type="application/json")

			else:
				subjectGroupDetail = topics_weekly_activity.objects.get(twid= data['twid'])
				subjectGroupDetail.noofsessions = data["noofsessions"]
				subjectGroupDetail.courseId = data["courseId"]
				subjectGroupDetail.showallsections = data["showallsections"]
				user = User.objects.get(id= data["modifiedBy"])
				subjectGroupDetail.modifiedBy = user
				subjectGroupDetail.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","twid":subjectGroupDetail.twid}),content_type="application/json")
		
		if(data["action"] == "allList"):
			subjectGroupObj = topics_weekly_activity.objects.filter(isActive=True)
			subjectGroupList = []
			for sg in subjectGroupObj:
				obj = {"id":sg.id,"twid":sg.twid,"noofsessions": sg.noofsessions,"courseId":sg.courseId,"showallsections":sg.showallsections}
				subjectGroupList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","data":subjectGroupList}),content_type="application/json")

		if(data["action"] == "delete"):
			subjectGroupDetail = topics_weekly_activity.objects.get(twid=data['twid'])
			subjectGroupDetail.isActive=False
			subjectGroupDetail.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")