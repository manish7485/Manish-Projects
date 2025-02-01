#Print Your Name As Many Times As You Want!
while True:
	try:
		name = input("Enter Your Name: ").capitalize().strip()
		num = 1
		number = int(input("Enter Number: "))
		while num <= number:
			print(f"{num}. {name}")
			num += 1
	except ValueError:
		print("Please Enter At Least 1 Value!")