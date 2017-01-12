# Create a patient class and a doctor class. Have a doctor that can handle 
# multiple patients and setup a scheduling program where a doctor can only 
# handle 16 patients during an 8 hr work day

class patients:
	def __init__(self):
		self.name = "Digle"

class doctor:
	def __init__(self):
		self.tot_patients = 0
	def scheduler(self):
		while self.tot_patients <= 16:
			self.hours = self.tot_patients/2.0
			print "%s patients served" %self.tot_patients
			print "%s of the 8 hr shift is used" %self.hours
			self.num = input("no of patients: ")
			self.tot_patients += self.num
			if self.tot_patients == 16:
				print "%s patients served" %self.tot_patients
				print "8 of the 8 hr shift is used"
				print "My shift is done!"
				break
			elif self.tot_patients > 16:
				self.temp = self.tot_patients - 16
				print "16 patients served"
				print "8 of the 8 hr shift is used"
				print "%s patients will have to be served by another doctor, my time is up" %self.temp

hospital=doctor()
hospital.scheduler()