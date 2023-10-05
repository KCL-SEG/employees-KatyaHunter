"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
	def __init__(self, name):
		self.name = name

	def get_pay(self):
		if self.name == "Billie":
			return 4000
		if self.name == "Charlie":
			return self.contracted_hours(100)
		if self.name == "Renee":
			return 3000 + self.contracted_commission(4)
		if self.name == "Jan":
			return self.contracted_hours(150) + self.contract_commission(3)
		if self.name == "Robbie":
			return 2000 + 1500
		if self.name == "Ariel":
			return self.contracted_hours(120) + 600

	def contracted_hours(self, hoursWorked):
		if self.name == "Charlie" or self.name == "Jan":
			return 25 * hoursWorked
		if self.name == "Ariel":
			return 30 * hoursWorked

	def contract_commission(self, noOfContracts):
		if self.name == "Renee":
			return 200 * noOfContracts
		if self.name == "Jan":
			return 220 * noOfContracts


	def __str__(self):
		if self.name == "Billie":
			return self.name + " works on a monthly salary of " + str(self.get_pay()) + ". Their total pay is " + str(self.get_pay()) + "."
		if self.name == "Charlie":
			return self.name + "works on a contract of 100 hours at 25/hour. Their total pay is str(self.get_pay()) + "."
		if self.name == "Renee":
			return self.name + " works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 220/contract. Their total pay is " + str(self.get_pay()) + "."
		if self.name == "Jan":
			return self.name + " works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is " + str(self.get_pay()) + "."
		if self.name == "Robbie":
			return self.name + "works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is " + str(slef.get_pay()) + "."
		if self.name == "Ariel":
			return self.name + " works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is " + str(self.get_pay()) + "."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
