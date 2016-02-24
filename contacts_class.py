class Contact(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_phone = ""
		self.work_phone = ""
		self.email = ""
		self.middle_name = ""

	def send_email(self, message):
		print "To: %s - %s" % (self.email, message)
