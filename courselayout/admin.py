# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import format_type, single_activity_type, single_activity, social_activity, topics_weekly_activity
from django.contrib import admin

# Register your models here.
admin.site.register(format_type)
admin.site.register(single_activity_type)
admin.site.register(single_activity)
admin.site.register(social_activity)
admin.site.register(topics_weekly_activity)