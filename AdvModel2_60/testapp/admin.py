from django.contrib import admin
from testapp.models import BaseClass,ChildClass1,ChildClass2
# Register your models here.
admin.site.register(BaseClass)
admin.site.register(ChildClass1)
admin.site.register(ChildClass2)
