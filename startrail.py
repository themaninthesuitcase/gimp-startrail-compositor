#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Gimp Startrail Compositor
# Version : 1.0
#
# Christopher Pearson
# http://code.google.com/p/gimp-startrail-compositor/
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

def startrail(width, height, frames, dark_frames,ext):
	#Do some santity checking before we start
	if len(frames) == 0:
		# print("No light frame path provided")
		return

	if not os.path.exists(frames):
		# print("light frame path doesn't exist")
		return

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

	for fileName in os.listdir(frames):
		if fileName.endswith(ext): 
			file = os.path.join(frames, fileName)
			# open the file as a new layer, then set the mode to lighten and then merge.
			new_layer = pdb.gimp_file_load_layer(image, file)
			new_layer.mode = 10 # lighten
			image.add_layer(new_layer,0)
			image.flatten()

	# If there is a specified path and that path exists then process the dark frames.
	if os.path.exists(dark_frames):
		for fileName in os.listdir(dark_frames):
			if fileName.endswith(ext): 
				file = os.path.join(dark_frames, fileName)
				# open the file as a new layer, then set the mode to difference and then merge.
				new_layer = pdb.gimp_file_load_layer(image, file)
				new_layer.mode = 6 # difference
				image.add_layer(new_layer,0)
				image.flatten()

	# done so clean up
	image.flatten()

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
		(PF_DIRNAME, "dark_frames","Dark Frames",""),
		(PF_STRING, "ext", "File extension (case sensitive)", "jpg" )
	],
	[],
	startrail,
	menu="<Image>/File/Create/Python-Fu",   
	domain=("gimp20-template", locale_directory) 
	)

main()
