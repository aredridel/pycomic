#Named after Mr Peabody from Peabody and Sherman
import os
import json

def initdef(defdirectory):
	comiclist =[]
	try:
		os.mkdir(defdirectory)
	except:
		print("Definition Directory already exists")
	#Reads definition files from the file directory
	for deffilename in os.listdir(defdirectory):
		comiclist.append(readdef())
	return comiclist
def readdef(deffilename):
	deffile = open(defdirectory +  "/" + deffilename, "r")
	defline = ""
	#list of the different things in a definition file
	deflist = ["comicname" ,"starturl", "nextregex", "imageregex", "rootcomicdir" ]

	#create and populate comicdef with placeholder values
	comicdef = []
	for item in deflist:
			comicdef.append( "#" + item)
	while True:
		#reads each line in the file, and writes it to comicdef 
		#until the last line is reached
		#except for the last two characters which are newline
		defline = deffile.readline()[:-1]
		#Process the definition file
		if defline == "":
			break
		else:
			for item in deflist:
				if defline[ : len(item)] == item:
					position = comicdef.index("#" + item)
					comicdef.remove("#" + item)
					comicdef.insert(position, defline[len(item)+1 : ])
	print(comicdef)
	return comicdef		
		
def initdir(comiclist, downloaddirectory):
	try:
		os.mkdir(downloaddirectory)
	except:
		print("Download Directory already exists")
	for comic in comiclist:
		try:
			os.mkdir(downloaddirectory + "/" + comic[0])
		except:
			print("Directory already exists for" + comic[0])
def initdb(downloaddir):
	try:
		db = open(downloaddir + "/.database", "x")
		db = open(downloaddir + "/.database", "w")
		json.dump(initdef("./def"), db)
	except:
		print("Database already exists")
	db = open(downloaddir + "/.database", "r")
	return json.load(db)	
def updatedb(comicname, newdef):
	db = open(downloaddir + "/.database", "w")
