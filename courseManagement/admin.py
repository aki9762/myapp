# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import sample,parentCategory,filesUpload,yesNo,forceLanguage,hiddenSection,formattbl,course,courseLayout,badges,competencyFramework,taxonomies

admin.site.register(parentCategory)
admin.site.register(filesUpload)
admin.site.register(yesNo)
admin.site.register(forceLanguage)	
admin.site.register(hiddenSection)
admin.site.register(formattbl)
admin.site.register(course)
admin.site.register(courseLayout)
admin.site.register(badges)
admin.site.register(competencyFramework)
admin.site.register(taxonomies)
admin.site.register(sample)