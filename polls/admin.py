from django.contrib import admin
from .models import Question
from .models import Choice
from .models import PSmessage
# Register your models here.

admin.site.register(Question) #向管理页面注册Question类别
admin.site.register(Choice)
admin.site.register(PSmessage)