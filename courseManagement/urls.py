from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

#load the view and the api's here
from courseManagement.views import(
	parentCategoryApi,
	getfileUplaod,
	getyesNo,
	getforceLanguage,
	getcourseLayout,
	gethiddenSection,
	getformattbl,
	courseApi,
	gettaxonomies,
	badgesApi,
	competencyFrameworkApi,
	subCategoryApi,
	userCoursesApi
	)

urlpatterns=[
url(r'^parentCategoryApi/$',parentCategoryApi,name="parentCategoryApi"),
url(r'^getfileUplaod/$',getfileUplaod,name="getfileUplaod"),
url(r'^getyesNo/$',getyesNo,name="getyesNo"),
url(r'^getforceLanguage/$',getforceLanguage,name="getforceLanguage"),
url(r'^getcourseLayout/$',getcourseLayout,name="getcourseLayout"),
url(r'^gethiddenSection/$',gethiddenSection,name="gethiddenSection"),
url(r'^getformattbl/$',getformattbl,name="getformattbl"),
url(r'^courseApi/$',courseApi,name="courseApi"),
url(r'^gettaxonomies/$',gettaxonomies,name="gettaxonomies"),
url(r'^badgesApi/$',badgesApi,name="badgesApi"),
url(r'^competencyFrameworkApi/$',competencyFrameworkApi,name="competencyFrameworkApi"),
url(r'^subCategoryApi/$',subCategoryApi,name="subCategoryApi"),
url(r'^userCoursesApi/$',userCoursesApi,name="userCoursesApi")
]
  
  