import os
import platform
import stat
cur_dir=os.getcwd()
os.system('echo "hello from sysetem command"')
print(f"Current working dir :{cur_dir} ")
file_size=os.stat("welcome.txt")
print(f"OSNAME IS: {os.name}")
print(f"platform IS: {platform.system()}")
print(f"Release IS: {platform.release()}")
print(f"CPU COUNT IS: {os.cpu_count()}")
print(f"The file permission of : {file_size}")
'''contents = os.listdir('.')
for item in contents:
	if os.path.isfile(item):
		get_size_files=os.path.getsize(item)
		print(f"the list of files are: {item} {get_size_files}KB" )
	#print(f"{files} and os.path.gesize({files})KB")

path = "D:\\Advance_Python\\listcomhe.py"
if os.path.exists(path):
	print(f"The {path} is Exists")
	if os.path.isfile(path):
		print(f"{path} is a file")
		get_file_size=os.path.getsize(path)
		print(f"The size of the file is : {get_file_size}KB")
	if os.path.isdir(path):
		print(f"{path} is a directory")
else:
	print(f"{path} does not exists")


contents = os.listdir('.')
for files in contents:
	print(files)
###########################################

files = [ f for f in os.listdir('.') if os.path.isfile(f)]
print(f"Files only: ",files) '''