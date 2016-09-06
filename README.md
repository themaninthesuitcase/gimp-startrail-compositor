**gimp-startrail-compositor** is a plugin for GIMP which automates the stacking of startrail images, producing either 1 or a set of stacked images.

# Installing the plugin

This plugin requires Python to work. On Linux and OSX this will be preinstalled but for Windows you will need to [install this separately](https://www.python.org/downloads/).

To install the plugin, copy the file `startrail.py` into a plugin folder of your choice. You can either place it in the default locations (see [below](#default-plugin-folders)), or my preference, by adding a plugin folder in my home directory to the plugins.

This last option can be done by going to Preferences :arrow_right: Folders :arrow_right: Plug-Ins.  Here you can add a new folder by clicking the new button (:page_facing_up:) and then navigating to the folder.  You will also be able to see the default locations used on this dialog.

Once done reload GIMP to have the changes take effect.

_The startrail.py script requires execute permissions for it to work.  If the plugin isn't working for you then check this first._

_On linux and macs this can be done by running `chmod +x startrail.py` from the plugins folder._

# Usage

Once installed the menu option can be found under File :arrow_right: Create :arrow_right: Startrail

![Menu bar](https://raw.githubusercontent.com/themaninthesuitcase/gimp-startrail-compositor/master/images/menu.png)

Once loaded you will be given 7 options to set:
* **Light Frames**: the folder containing all your light frames, i.e. the ones you can see the stars in.
* **Use Dark Frames**: Do you want to use dark frame noise reduction
* **Dark Frames**: the folder containing all your dark frames, i.e. the ones you took with the lens cap on.
* **Save intermediate frames**: Checking this will save an image after each frame is layered, allowing you to make a time lapse of the trail building up.
* **Intermediate save directory**: The directory to save the intermediate frames to.  They will be named trail00001.jpg, trail00002.jpg and so on.
* **Live display update *(MUCH slower)***: This will display the frames to the screen live as they are stacked together.  This slows the process down considerably, around 3-4 times slower.  Because of the speed issue, this is disabled by default.
* **Merge all images into a single layer**: This will merge each layer into 1 final image as the stacking progresses.  Disabling this will leave each image in it's own layer. This will add a lot more time to the stack and use more memory but gives more options in post processing.
* **Automatically remove skyglow**: Attempts to reduce the effect of sky glow by creating a copy of each light frame and applying a heavy blur.  This is then subtracted from the light frame before stacking.  The theory being the blur removes the detail leaving only the sky glow which can then be removed.  See this article for detail on how this works: [Creating star trails with automatic sky glow removal](http://fstop138.berrange.com/2016/08/creating-star-trails-with-automatic-sky-glow-removal/).  This will approximately double the time to process each frame.

![Options dialog](https://raw.githubusercontent.com/themaninthesuitcase/gimp-startrail-compositor/master/images/controls.png)

Currently the plug-in will look for files with the following file extensions:
jpg, jpeg, tiff, tif, bmp and png.

Once all your options are set click ok and wait for the plug-in to do its work.

Once done you will get a new image made from your source images, though this is not saved yet unless you enabled _Save intermediate frames_ where it will be the last frame saved.

![Sample stacked image](https://github.com/themaninthesuitcase/gimp-startrail-compositor/raw/master/images/GimpTrail800.png)

This is an example of a timelapse made using intermediate frames:
http://www.youtube.com/watch?v=Qaw72e93JA4
