import hashlib
from difflib import SequenceMatcher

# function to return the msg of files
def hash_file(file1, file2):

# using hashlib module to store hash of files
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

# read the contents of file_1 in binary mode 
    with open ("p1.pdf", "rb") as f_1:
        chuck = 0
        for i in range(chuck!=b''):
            chunck = f_1.read(1024)
            h2.update(chunck)

# read the contents of file_2 in binary mode
    with open ("p2.pdf", "rb") as f_1:
        chuck = 0
        for i in range(chuck!=b''):
            chunck = f_1.read(1024)
            h1.update(chunck)

    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_file("p1.pdf", "p2.pdf")


if(msg1!= msg2):
    print("The files are not identical")

else:
    print("The files are identical")