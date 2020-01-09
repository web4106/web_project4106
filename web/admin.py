from django.contrib import admin

# Register your models here.

from mptt.admin import MPTTModelAdmin
from web.models import *

admin.site.register(GoodsType, MPTTModelAdmin)
admin.site.register(UserProfile)