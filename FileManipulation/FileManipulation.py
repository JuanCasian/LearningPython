import time
import shutil
from shutil import make_archive
from zipfile import ZipFile
import os
from os import path

file1 = open("testfile1.txt", "w+")
file1.write("Hello World!")
file1.close()

file2 = open("testfile2.txt", "w+")
file2.write("Some Lorem to test:\n")
file2.close()

file2 = open("testfile2.txt", "a")
file2.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \nExcepteur sint occaecat cupidatat non proident, \nsunt in culpa qui officia deserunt mollit anim id est laborum.")
file2.close();

file2 = open("testfile2.txt", "r")
lines = file2.readlines()
file2.close()
i = 0
for line in lines:
    i = i + 1
    print("This is line number " + str(i))
    print(line)

for n in range(10):
    filename = "file" + str(n) + ".yes"
    file3 = open(filename, "w+")
    file3.write("LOLOLOL")
    file3.close()

print("Files were created, you have 5 secs before they are deleted, but don't worry they are gonna be safe in zip file");
time.sleep(5)

with ZipFile("testZip.zip", "w") as newzip:
    for n in range(10):
        filename = "file"+str(n)+".yes"
        if (path.exists(filename) and path.isfile(filename)):
            newzip.write(filename)

for n in range(10):
    filename = "file"+str(n)+".yes"
    if (path.exists(filename) and path.isfile(filename)):
       os.remove(filename)
    print(filename + " was deleted")


