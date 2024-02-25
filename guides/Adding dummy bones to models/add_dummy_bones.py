###############################################################
# by Crowfunder                                               #
# Copyright my ass but also the GPL-3.0 License               #
# Github: https://github.com/Crowfunder                       #
###############################################################

# Read xml file
filename = str(input("Input file name/path: "))
if '.xml' not in filename:
    filename += '.xml'

with open(filename, 'r') as file:
  filedata = file.read()
  
 
# Armature data modification
def ret_dummy_bone(number):
    return f"<entry> <name>dummy_bone{number}</name> <transform> </transform> <children> </children> </entry> "
    
def ret_dummy_name(number):
    return f",dummy_bone{number}"


armature_hook = "<root>\n      <name>%ROOT%</name>\n      <transform>\n      </transform>\n      <children>"
bones_hook = "</bones>"
armature_modified = armature_hook
bones_modified = bones_hook

dummies_num = int(input("How many dummy bones do you want to add: "))
for i in range(0, dummies_num):
    armature_modified += ret_dummy_bone(i)
    bones_modified = ret_dummy_name(i) + bones_modified

filedata = filedata.replace(armature_hook,  armature_modified)
filedata = filedata.replace(bones_hook,     bones_modified   )

# File return
new_filename = 'dummybone_' + filename
with open(new_filename, 'w') as file:
  file.write(filedata)