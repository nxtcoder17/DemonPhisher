from Websites import Sites
def menu():
	# Ascii Art generated through URL: http://www.kammerl.de/ascii/AsciiSignature.php
	# Fonts Name: wetletter

	print ("+------------------------------+")
	print ("| Choose one of the Following: | ")
	print ("+------------------------------+")
	counter = 1;
	for item in Sites.sites:
		print (f"\t[{counter}]: {item[0]}")
		counter += 1;

	while True:
		try:
			choice = int(input("\t\tEnter Your Choice: "))
		except ValueError:
			print ("You typed something that is not an Integer, Try Again ...\n")
		else:
			if (choice < 1 or choice >= counter):
				print ("Invalid Choice, Try Again ....\n")
			else:
				break

	return choice

if __name__ == '__main__':
	menu()
