# What is it?
Bones can be used for attachments and transform targets in animations. This script creates a few dummy bones that are not affected by any vertices or animations, unless for some reason the model already has bones named "dummy\_bone69" etc.

# Requirements
- Python3
- Spiralview

# Usage
1. In Spiralview, open the model you wish to add bones to.
2. Press `Edit`, in the menubar of the new pop-up window press `File > Export to XML...`, make sure to add .xml extension to the name.
3. Place the script in the location of the exported XML, run it and input the full file name of the exported .xml (i.e `exported_model.xml`) 
OR
3. Run the script and input the full path to the exported .xml (i.e `C:/Users/Parma/exported_model.xml`) (Use slashes `/` instead of backslashes `\`)
4. Pick how many dummy bones you want to create
5. A new xml file with "dummybone\_" prefix will be created. 
6. In Spiralview, press CTRL+R
7. In the new pop-up window menubar press `File > Import from XML...`
8. Choose the .xml file with `dummybone_` prefix
9. In the pop-up window menubar press `File > Save As` and save the modified model.
