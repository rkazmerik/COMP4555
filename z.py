vacations = []
polling_active = True

while polling_active:
	vacation = input("What is your dream vacation? ")
	vacations.append(vacation)

	repeat = input("Would you like to add another dream vacation? (yes/ no) ")

	if repeat == 'no': 
		polling_active = False

for vacation in vacations:
	print(f"You would like to: {vacation}")

