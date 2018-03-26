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
from coursecontent.models import pagecontent

# Create your views here.

@api_view(['POST'])
def createpagecontent(request):
	try:
		# return HttpResponse(json.dumps({"responsecode":id}))
		
		data = request.data
		if(data["action"]=="create" or data["action"]=="edit"):
			if(data['pcid'] == ""):
				pagec = pagecontent()
				pagec.name = data["name"]
				pagec.desc = data["desc"]
				pagec.showdesc = data["showdesc"]
				pagec.pcontent = data["pcontent"]
				pagec.displayname = data["displayname"]
				pagec.displaydesc = data["displaydesc"]
				pagec.tracking = data["tracking"]
				pagec.requireviewactivity = data["requireviewactivity"]
				pagec.recivegradetocomplete = data["recivegradetocomplete"]
				pagec.submittocomplete = data["submittocomplete"]
				pagec.completedondate = data["completedondate"]
				pagec.tags = data["tags"]
				pagec.coursecompitancies = data["coursecompitancies"]
				pagec.uponactivitycompitancy = data["uponactivitycompitancy"]
				user = User.objects.get(id= data["createdBy"])
				pagec.createdBy = user
				pagec.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","pcid":pagec.pcid}),content_type="application/json")

			else:
				pagec = pagecontent.objects.get(pcid= data['pcid'])
				pagec = pagecontent()
				pagec.name = data["name"]
				pagec.desc = data["desc"]
				pagec.showdesc = data["showdesc"]
				pagec.pcontent = data["pcontent"]
				pagec.displayname = data["displayname"]
				pagec.displaydesc = data["displaydesc"]
				pagec.tracking = data["tracking"]
				pagec.requireviewactivity = data["requireviewactivity"]
				pagec.recivegradetocomplete = data["recivegradetocomplete"]
				pagec.submittocomplete = data["submittocomplete"]
				pagec.completedondate = data["completedondate"]
				pagec.tags = data["tags"]
				pagec.coursecompitancies = data["coursecompitancies"]
				pagec.uponactivitycompitancy = data["uponactivitycompitancy"]
				user = User.objects.get(id= data["modifiedBy"])
				pagec.modifiedBy = user
				pagec.save()

				return HttpResponse(json.dumps({"responsecode":"200","status":"Success","pcid":pagec.pcid}),content_type="application/json")
		
		if(data["action"] == "allList"):
			subjectGroupObj = pagecontent.objects.filter(isActive=True)
			subjectGroupList = []
			for sg in subjectGroupObj:
				obj = {"id":sg.id,"pcid":sg.pcid,"name":sg.name,"desc":sg.desc,"showdesc":sg.showdesc,"pcontent":sg.pcontent,"displayname":sg.displayname,"displaydesc":sg.displaydesc,"tracking":sg.tracking,"requireviewactivity":sg.requireviewactivity,"recivegradetocomplete":sg.recivegradetocomplete,"submittocomplete":sg.submittocomplete,"completedondate":sg.completedondate.isoformat(),"tags":sg.tags,"coursecompitancies":sg.coursecompitancies,"uponactivitycompitancy":sg.uponactivitycompitancy}
				subjectGroupList.append(obj)
			return HttpResponse(json.dumps({"responsecode":"200","status":"success","data":subjectGroupList}),content_type="application/json")

		if(data["action"] == "delete"):
			pagec = pagecontent.objects.get(pcid=data['pcid'])
			pagec.isActive=False
			pagec.save()
			return HttpResponse(json.dumps({"responsecode":"200","status":"success"}),content_type="application/json")

	except Exception as e:
		return HttpResponse(json.dumps({ "status" : False, "responce code":"500","error":str(e) }), content_type="application/json")