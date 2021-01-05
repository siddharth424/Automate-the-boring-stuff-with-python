### Chapter-10

##### 1. What is the difference between shutil.copy() and shutil.copytree()?
shutilcopy() is used to copy a single file whereas shutil.copytree() will copy entire folder.

##### 2. What function is used to rename files?
shutil.move()
It is moved to the same place with different name.

##### 3. What is the difference between the delete functions in the send2trash and shutil modules?
send2trash will move the file to recycle bin(Temporary delete).
shutil functions will permanently delete.

##### 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
zip.ZipFile()
