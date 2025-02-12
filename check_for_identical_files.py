import hashlib
from difflib import SequenceMatcher

# function to return the msg of files
def hash_file(file1, file2):

# using hashlib module to store hash of files
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

# read the contents of file_1 in binary mode 
    with open (file1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

# read the contents of file_2 in binary mode
    with open (file2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
# returning the output of the funtion
    return h1.hexdigest(), h2.hexdigest()

# output of the function
msg1, msg2 = hash_file("p1.pdf", "p1 copy.pdf")

# last condition to check for the output
if(msg1!= msg2):
    print("The files are not identical")

else:
    print("The files are identical")