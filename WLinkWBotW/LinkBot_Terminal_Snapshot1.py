# Start of script
"""
L I N K B O T WWW
T E R M I N A L 1
-----------------
V E R S I O N 001
"""
# Definitions
def aboutLinkBot(): # Assigned to "A"
	print ("About Link Bot")
	print ("Link bot (WWW Link Bot/WLinkWBotW)")
	print ("Web crawler and ripper")
	print ("* Finds dead links")
	print ("* Archives web page")
	print ("* Has many settings")
	print ("* Rips websites")
	noMore = input("Press [ENTER] key to continue")
def settingsMenu(): # Assigned to "B"
	print ("Linkbot settings")
	print ("* NOT FOUND")
	noMore = input("Press [ENTER] key to continue")
def crawlstart(): # Assigned to "C"
	print ("LinkBot crawling")
	URLInput = str(input("Enter a URL to crawl:"))
	print ("Failed to crawl link, client out of date")
	noMore = input("Press [ENTER] key to continue")
def ripStart(): # Assigned to "D"
	print ("LinkBot ripping")
	URL2Input = str(input("Enter a URL to rip: "))
	print ("Expected size: 0 petabytes (0 terabytes) (0 gigabytes) (0 megabytes) (0 kilobytes) (0 bytes) (0 bits)")
	print ("Files ripped: 0/0")
	print ("Ripping process cancelled, client out of date")
	noMore = input("Press [ENTER] key to continue")
def viewArchives(): # Assigned to "E"
	print ("Archive library")
	print ("000001 | https://www.example.com")
	print ("000002 | ---")
	print ("End of list")
	noMore = input("Press [ENTER] key to continue")	
def viewStatus():  # Assigned to "F"
	print ("LinkBot status")
	print ("Client: V1 (Out of date)")
	print ("Can crawl: No")
	print ("Written in: Python")
	print ("Compatible with: Python 3.5, Python 3.6, Python 3.6.1, Python 3.6.2, Python 3.6.3, Python 3.7, Python 3.7.1, Python 3.7.2")
	print ("No more data available")
	noMore = input("Press [ENTER] key to continue")	
def null_1():  # Assigned to "G"
	print ("Other/unknown")
	noMore = input("Press [ENTER] key to continue")	
def linkBotHelp():  # Assigned to "H"
	print ("LinkBot help")
	print ("- Crawling")
	print ("- Ripping")
	print ("- Settings")
	print ("Unable to access help, cleitn out of date")
	noMore = input("Press [ENTER] key to continue")
# End of definition section
print ("LinkBot Terminal")
l = float(3.14)
while (l == l): # Loops the terminal
	print ("ID list")
	print ("A - About")
	print ("B - Settings")
	print ("C - Start crawling")
	print ("D - Start ripping")
	print ("E - View archives")
	print ("F - View status")
	print ("G - Other")
	print ("H - Help")
	input1 = str(input("Enter a letter ID to continue"))
	input1 = input1.upper() # Makes input uppercase, easier compatibility with ID list
	print ("You selected " + str(input1))
	if (input1 == "A"):
		print (aboutLinkBot())
	if (input1 == "B"):
		print (settingsMenu())
	if (input1 == "C"):
		print (crawlStart())
	if (input1 == "D"):
		print (ripStart())
	if (input1 == "E"):
		print (viewArchives())
	if (input1 == "F"):
		print (viewStatus())
	if (input1 == "G"):
		print (null_1())
	if (input1 == "H"):
		print (linkBotHelp())
	#else if not ((input1 == "A") or (input1 == "B") or (input1 == "C") or input1 == "D") or (input1 == "E") or (input1 == "F") or (input1 == "G") or (input1 == "H")): # Doesn't work
	else:
		print ("Invalid ID")
		continue1 = input("Press [ENTER] key to try again")
print ("Program unexpectedly stopped") # If somehow the terminal failed to keep looping (likely from modification) this message will pop up, and you will have to leave the terminal
noMore = input("Press [ENTER] key to quit")
''' File stats
Line count: 00,.109
Character count: 003,.991
Size: 003,.991 bytes (003,.991 Kilobytes) (000,.003 Megabytes)
File format: *.py (Python file)
Version: 1 (September 23rd 2019)
First version: 1 (September 23rd 2019)
Python version compatibility: 3.5-3.7.2
Software type: Free, Open-Source
Sharing status: Share and modify as you please, as long as you give credit, you can do what you want with it
License: None yet
Encoding: UTF-8 with no Unicode characters
'''
# End of script