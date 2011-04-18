#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Gimp Startrail Compositor
# http://code.google.com/p/gimp-startrail-compositor/
# Version : 1.1
#
# Christopher Pearson
# www.cpearson.me.uk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from gimpfu import *

import gettext
locale_directory = gimp.locale_directory
gettext.install( "gimp20-template" , locale_directory, unicode=True )

allowedTypes = ["jpg","jpeg","tiff","tif","bmp","png"]

def createStarterImage(width, height):
	# Create a new image to work in.
	image = gimp.Image(width, height, RGB)

	# Create a new layer to form our background
	bg = gimp.Layer(image, "", width, height, RGB_IMAGE, 100, NORMAL_MODE)
	image.add_layer(bg, 0)
	# Save off the old BG colour as they may want to keep it.
	old_background = gimp.get_background()

	# Fill the new layer with black so the lighten process works.
	gimp.set_background(0, 0, 0)
	bg.fill(BACKGROUND_FILL)

	# put the old background back.
	gimp.set_background(old_background)

	# We're done messing with the background so flatten down.
	image.flatten()
	return (image)	
	
def processImage(fileName, image, layerMode):
	ext = os.path.splitext(fileName)[1] # get the extension
	ext = ext.replace(".", "") # rip off the . from the extension
	if ext.lower() in allowedTypes: # is this an image?
		newLayer = pdb.gimp_file_load_layer(image, fileName)
		newLayer.mode = layerMode
		image.add_layer(newLayer,0)
		image.flatten()

def startrail(width, height, frames, dark_frames):
	#Do some santity checking before we start
	if len(frames) == 0:
		pdb.gimp_message("No light frame path provided.")
		return

	if not os.path.exists(frames):
		pdb.gimp_message("Light frame path doesn't exist.")
		return

	# Create a new image to work in.
	image = createStarterImage(width, height)

	for fileName in os.listdir(frames):
		processImage(os.path.join(frames, fileName), image, 10) # Lighten mode.
	
	# If there is a specified path and that path exists then process the dark frames.
	if os.path.exists(dark_frames):
		for fileName in os.listdir(dark_frames):
			processImage(os.path.join(dark_frames, fileName), image, 6) # Difference mode.
			
	# show the new image
	gimp.Display(image)

register(
	"startrail",
	"",
	"",
	"Christopher Pearson",
	"GPL v3",
	"2011",
	_("Startrail"),
	"",
	[
		(PF_INT, "width", "Width",3008),
		(PF_INT, "height", "Height",2000),
		(PF_DIRNAME, "frames","Light Frames",""),
		(PF_DIRNAME, "dark_frames","Dark Frames","")
	],
	[],
	startrail,
	menu="<Image>/File/Create/Python-Fu",   
	domain=("gimp20-template", locale_directory) 
	)

main()
