# create a new process
# Python code to create child process
### Mert Furkan Ergüden 170709015
import os
import requests
import multiprocessing
import urllib
import hashlib
import uuid

def ParentProcess():
	print("Parent Process is starting")
	parent_pid = os.getpid()
	print(parent_pid)


url =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
		"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
		" https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg ",
		" http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg ",
		 " https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg "]

def download_file(url,file_name=None):

    r = requests.get(url, allow_redirects=True)
    filename = file_name if file_name else str(uuid.uuid4())## file name is randomly
    open(file,"wb").write(r.content) ## open th donloaded file
    current_directory= os.getcwd()# working on these directory
    print(current_directory) ### print current directory
    duplicate_checking()

def ChildProcess(url):
	print("child ChildProcess is starting")
	child_pid = os.getpid()
	print(child_pid)    #print to child pid
    for i in range(0,len(url)):
		download_file(url[i])


def duplicate_checking():

    duplicates = [] ## thats going to store all the duplicates files. list.
    has_keys = dict() ##
    for index, filename in enumerate(os.listdir('.')): ##count each iteration
        if os.path.isfile(filename):
            with open(filename,'rb') as f:
                filename = hashlib.md5(f.read().hexdigest())##using md5 for each file
            if filenamehas not in hash_keys:
                hash_keys[filename]=index ## create new key and stored has_keys dict()
            else:
                duplicates.append((index,hash_keys[filehash]))
## bu kodların ardından duplicates  listesini bastırdıgımızda  duplicate olanları tutar ve gösterir.
## end of removing duplicate images using hashing
files_list = os.listdir()##list of the all files located
##delete files after printing:
for index in duplicates:
    os.remove(files_list[index[0]]) ##remove duplicate files

#Question1
#Thus executing os.fork() creates two processes: A parent process and a child process.
retVal = os.fork() #os.fork() when called from a program it creates a new process.
print("Return value is %d"%(retVal))
# Separate logic for parent and child
if retVal == 0: ##call the ChildProcess()
	ChildProcess()
else: ####call the  ParentProcess()
    os.wait() #avoid the orphan process situation
    ParentProcess()

    
    
    

