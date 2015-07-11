from django.db import models
import datetime
from django.utils import timezone
import uuid

# Create your models here.

class DeviceType(models.Model):
	'''Tells what kind of device this is'''
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Device(models.Model):
	'''A single iot node, it's important properties, and commands that can be run on it
		Might consider using mongodb for this...actually.  IDK.  Toss up between that
		and moving everything to Cassandra
	'''
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	device_type = models.ForeignKey(DeviceType)
	# variables that are exposed to IoT on this device
	# ex: temperature_f, temperature_c, humidity, ...
	variables = models.CharField(max_length=2048)
	# commands that can be run against this device (to run motors, switch things, etc)
	# syntax: "command(arg1,arg2,arg3)" this might/probably will change
	commands = models.CharField(max_length=2048)
	created = models.DateTimeField(auto_now_add=True)	

	def __unicode__(self):
		return self.name

class DeviceData(models.Model):
	'''Represents a data point for a specific device variable in time'''
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	device = models.ForeignKey(Device)
	variable = models.CharField(max_length=128)
	# No idea what type of data will be stored, really
	# Might have to do some type juggling to handle types later, not sure
	value = models.CharField(max_length=2048)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.field

