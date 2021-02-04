from django.contrib import admin
from .models import * 


admin.site.site_title = "အာဏာရှင်ဆန့်ကျင်ရေး အချက်အလက်များ"
admin.site.site_header = "အာဏာရှင်စနစ်ကိုကန့်ကွက်ကြောင်း နည်းပညာကျောင်းသား ကျောင်းသူများမှ စုစည်းတင်ပြချက်"
admin.site.index_title = "အာဏာရှင်ဆန့်ကျင်ရေး အချက်အလက်များ"

from django.contrib import admin
from django.contrib.auth.models import Group, User 

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(ချိုးဖောက်မှုပုဒ်မများ)
admin.site.register(အချက်အလက်များ)
admin.site.register(ထောက်ခံချက်များ)