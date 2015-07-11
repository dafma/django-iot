# not used in this (iot) project now.  Needs a new home.
import RPi.GPIO as GPIO

class RPIDigitalPin:

	pin = None
	up_down = None
	bouncetime = None
	rising_callback = None
	falling_callback = None


	def __init__(self, pin, rising_callback, falling_callback, up_down=GPIO.PUD_DOWN, bouncetime=300):
		self.pin = pin
		self.rising_callback = rising_callback
		self.falling_callback = falling_callback
		self.up_down = up_down
		self.bouncetime = bouncetime

	def risingCallback(self, channel):
		print channel
		self._setFallEvent()
		self.rising_callback(channel)

	def fallingCallback(self, channel):
		print channel
		self._setRiseEvent()
		self.falling_callback(channel)

	def setup(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.IN, self.up_down)
		if self.up_down == GPIO.PUD_DOWN:
			self._setRiseEvent()
		else:
			self._setFallEvent()

	def _setRiseEvent(self):
		GPIO.remove_event_detect(self.pin)
		GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.risingCallback, bouncetime=self.bouncetime)

	def _setFallEvent(self):
		GPIO.remove_event_detect(self.pin)
		GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.fallingCallback, bouncetime=self.bouncetime)