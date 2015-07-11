from django.contrib import admin
from iot.models import Device, DeviceType, DeviceData

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'variables', 'commands', 'device_type', 'created')
	search_fields = ['name']

class DeviceTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ['name']

class DeviceDataAdmin(admin.ModelAdmin):
	list_display = ('device', 'variable', 'value', 'timestamp')
	search_fields = ['device']

# Register your models here.
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(DeviceData, DeviceDataAdmin)