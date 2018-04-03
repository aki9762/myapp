# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django import forms
from courseManagement.models import course
import csv
import django_excel as excel
from django.http import HttpResponseBadRequest, HttpResponse
import datetime
import ast
from datetime import datetime

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

########################################### class required while importing data ###########################################
class UploadFileForm(forms.Form):
    file = forms.FileField()



######################################### import_sheet to database ##########################################
def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
      
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
        	
        	request.FILES['file'].save_to_database(
                name_columns_by_row=1,
                model=course,
                mapdict=[
                			'courseId',
							'courseCategoryId',
							'fullName',
							'shortName',
							'visibility',
							# 'startDate',
							# 'endDate',
							'summary',
							'formatId',
							'numberOfSection',
							'hiddenSectionId',
							'courseLayoutId',
							'forceLanguageID',
							'numOfAnnounment',
							'showGradesToStudent',
							'showActivityReport',
							'enableCompletionTracking',
							'maxUploadSize',
							'createdBy',
							'ModifiedBy'
						])
        	return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})
