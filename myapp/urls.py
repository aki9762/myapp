"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import rest_framework_jwt.views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api/auth/token', rest_framework_jwt.views.obtain_jwt_token),
	url(r'^courselayoutapi/', include('courselayout.urls')),
	url(r'^api/courseManagement/',include("courseManagement.urls", namespace="courseManagement-api")),
	url(r'^coursecontent/',include("coursecontent.urls")),
	url(r'^$', schema_view),
	url(r'^docs/', include('rest_framework_docs.urls')),
	url(r'^api/impexp/',include("impexp.urls", namespace="impexp-api"))
]
