**Requirements:**
GIMP: https://www.gimp.org/
SpiralView: https://github.com/lucas-allegri/spiralview

**Abbreviations:**
RMB - Right mouse button

# GIMP

1. Top menubar, Image > Mode, change from Indexed to RGB
2. Top left side of the window, Select by color tool (three circles and square icon, you may need to RMB on the "Fuzzy Select" tool). By holding shift you can select multiple times and add to selection, and by holding Ctrl you substract from selection.
3. RMB on image > Edit > Copy (Ctrl+C)
4. RMB on image > Edit > Paste As > New Layer In Place
5. Right side of the window, right above the list of layers and "Opacity", click on "Mode" dropdown menu, scroll down and select HSV Hue
6. RMB on the image > Colors > Colorize
7. Click on the colored "Color" bar, in "HTML notation" box input "ff00ff", press "OK", press "OK"
8. Right side of the window, in the list of layers, RMB on the topmost layer > Merge Down
9. Top menubar, Image > Mode, change from RGB to Indexed, in the new window press "Convert"
10. Top menubar, File > Save just in case (Ctrl+S), File > Export the file (Ctrl+E), in the new window pick a filename and a folder and press export

That concludes the GIMP part.

# SpiralView

1. Replace the model texture in SK files with the texture you created.
2. Open SpiralView, Model Editor, open the model of the thing you want to be prismatic, once you do press Edit. On top of the new window you will see "Type" dropdown menu, if it's not "Compound" or "Conditional", you're good, but if it's not, then your model is probably a different file, and this file is merely a wrapper, **although remember this file, you will need it later.**
3. Find the "Material Mappings" section, find the material mapping with the texture you just replaced (find its filename). Remember the number next to it, it will be important later on, for now let's assume it's "Material Mappings (0)", so the number is 0
4. Right above the button with the texture filename, click on the button next to "Config: "
5. In the new window, find "Colorized (Single)" folder, if it's closed double click on it and select "Default" underneath.
6. Scroll down to the very bottom of the file, to the "Parameters" section
7. Press "New Parameter", Name it "Colorization". In the paths press "New" and, remembering that "0" stands for the number from earlier, so you may have to change it, paste `implementation.material_mappings[0].material["Texture"]["Colorization"]` for each prismatic material mapping. **Important note here, if earlier you noticed that model is wrapped in a different model, such as Compound or Conditional, you'll need to complete the "Extra Step", if the model stays magenta after all the steps, you may need to look for such wrapper that contains the model and is Conditional/Compound**

Congratulations, your model should be prismatic.

# The Extra Step
1. Look for the model that wraps the model you edited earlier, it should be anything but Articulated or Static that has models within itself, something like Conditional, Derived or Compound.
2. Once you find it, press Edit, in the new window, you will be creating a parameter. Tree View may be useful (press "View" in the top menubar)
3. Click through all the folders until you encounter your edited, prismatic model path.
4. In "Parameters" create a "Colorization" parameter, from the top of the file trace back the path of the model, such as shown in example, and input the created parameter.

Example: Let's assume we've got a model that's bundled in a compound model (item/gear/helm/grem/model\_seerus.dat) 
We're going from top, topmost node is "implementation", within it we've got "influences", "models" and "parameters", the first one obviously doesn't contain our model, nor does the last one, so it should be "Models". 
"Models" contains potentially a couple different models, we need to find the one with "Colorization", in our case it's "Models (0)". 
Now we've got all the info, we need to access our model's "Colorization" through a parameter. start with "Implementation", then from "Models" array select model with index 0, and in this model access "Colorization" parameter. 

Hence, `implementation.models[0].model["Colorization"]`