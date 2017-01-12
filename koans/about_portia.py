#coding: utf-8
from runner.koan import*
from koan_labs.portia import*
from math import floor

class AboutPortia(Koan):
	def test_about_portia(self):
		"""
		This activity will help you understand how to use while loops
		QUESTION
		In the year 0 A.D., my ancestor Brutus Balkcom deposited 1.00 in the Bank of Rome. 
		OK, it wasn’t a real dollar- it was the Roman equivalent of a dollar. Probably some kind of big coin 
		with a hole in the middle. The bank promised to pay 5 percent interest compounded once a year.
		In other words, they multiplied his balance by 1.05 once each year, so that
		at the end of the year 1 A.D., the balance was $1.05.
		at the end of the year 2 A.D., the balance was $1.1025 (which is 1.05 × 1.05).
		at the end of the year 3 A.D., the balance was $1.157625 (which is 1.1025 × 1.05).
		Since old Brutus was not around to withdraw it (Caesar’s descendants took care of that),
		the balance has accumulated nicely up to the present day. Because I am his rightful heir,
		the bank account is now mine. Bwa-ha-ha!!
		__________
		ACTIVITY 1
		__________

		Your first job is to write a Python program that computes my current wealth: the balance of the account
		after 5 percent interest was compounded 100 times.
		
		
		The first thing you need to do is create a function named calculate_wealth in (koan_labs/ portia.py) which takes the 
		parameter CurrentYear, in this case is 100.
		Inside the function create three variables You can name them however you want to.
		I used, CurrentWealth=1, Year=0 and rate of interest which i assigned .05 to.
		After that create a while loop that ensures that the Year doesn't exceed the CurrentYear
		which in this case is 100. Inside the while loop, increment the year by 1 everytime and increment the CurrentWealth
		by multiplying it by the interest.
		Something like CurrentWealth+=CurrentWealth*Interest. Finally, return the amount but first import the floor function and 
		use it on the amount

		"""
		self.assertEqual(calculate_wealth(100),131.0,"The expected result is 131.0")


	def test_about_kaya(self):
		"""

		In a coincidence that defies the odds, our section leader Kaya Thomas has an ancestor, Portia Thomas, 
		who also deposited money in the Bank of Rome in the year 0 A.D.
		Back then, the Thomas family was much better off than the Balkcom family, and Portia deposited $100,000.00.
		But Portia did not know that in business, you don’t get what you deserve – you get what you negotiate – and 
		she was able to get only a 4 percent interest rate on her deposit.
		Your job is to write a Python program that computes the first year in which Brutus’s balance exceeds Portia’s
		balance, and RETURNS THAT YEAR.


		__________
		ACTIVITY 2
		__________
		
		In this problem, I created a function named find_year in koan_labs/portia.py that takes no parameter. I created three 
		variables namely: wealthportia = 100000, wealth= 1, numberofyears= 1.
		I then created a while loop that executes as long as wealth does not exceed wealthportia.
		Inside that while loop, i incremented number of years by one every time
		I also had two other lines of code, One would increase wealth depending on the rate of interest yearly - 
		something like wealth= 1.05* (float(wealth))
		While the other would increment wealthportia depending on the interest as well.
		If wealth exceeds wealthportia, it should return the year when the wealth exceeded wealthportia.

		"""
		self.assertEqual(find_year(), 1205, "The expected result is 1205")
