#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Gimp Startrail Compositor
# http://code.google.com/p/gimp-startrail-compositor/
# Version : 1.2
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
LIGHTEN = 10
DIFFERENCE = 6

def fileIsImage(fileName):
	isImage = 0
	ext = os.path.splitext(fileName)[1] # get the extension
	ext = ext.replace(".", "") # rip off the . from the extension
	if ext.lower() in allowedTypes: # is this an image?
		isImage = 1
	return(isImage)
		
def processDarkFrame(fileName, image, layerCount):
	darkFrame = pdb.gimp_file_load(fileName,"")
	
	# have we got a base image to work with?
	if image == None:
		# create a base image based on the dark frame
		image = pdb.gimp_image_new(darkFrame.active_layer.width, darkFrame.active_layer.height, 0)
		
	# get the main layer of the new frame
	darkLayer = pdb.gimp_layer_new_from_drawable(darkFrame.active_layer, image)
	# set the opacity to half that of the one before so we get an average
	darkLayer.opacity = 100.0 / layerCount
	# add the new layer and flatten down to keep memory useage down.
	image.add_layer(darkLayer,0)
	image.flatten()
	# Get rid of the image we loaded up.
	gimp.delete(darkFrame)
	return(image)

def createDarkImage(darkFrames):
	darkImage = None	
	layerCount = 1
	
	for fileName in os.listdir(darkFrames):
		fileName = os.path.join(darkFrames, fileName)
		if fileIsImage(fileName):
			darkImage = processDarkFrame(fileName, darkImage, layerCount)
			layerCount += 1
	
	return darkImage

def processLightFrame(fileName, image, darkImage):
	# load up the light frame into an image
	lightFrame = pdb.gimp_file_load(fileName,"")
	
	# have we got a base image to work with?
	if image == None:
		# create a base image based on the light frame
		image = pdb.gimp_image_new(lightFrame.active_layer.width, lightFrame.active_layer.height, 0)			

	# did we make a dark frame?
	if darkImage != None:
		# As we have a dark image we need to difference it against the light frame.
		# create a new layer from the dark image
		darkLayer = pdb.gimp_layer_new_from_drawable(darkImage.active_layer, lightFrame)
		# set the layer to difference
		darkLayer.mode = DIFFERENCE
		# add the layer to the lightFrame
		lightFrame.add_layer(darkLayer, 0)
		# flatten
		lightFrame.flatten()
				
	# Set the light frame to lighten 
	lightLayer = pdb.gimp_layer_new_from_drawable (lightFrame.active_layer, image)
	lightLayer.mode = LIGHTEN
	# add this as new layer
	image.add_layer(lightLayer,0)
	image.flatten()
	
	# clean up our temp bits.
	gimp.delete(lightFrame)
	return(image)

def startrail(frames, darkFrames):
	#Do some santity checking before we start
	if len(frames) == 0:
		pdb.gimp_message("No light frame path provided.")
		return

	if not os.path.exists(frames):
		pdb.gimp_message("Light frame path doesn't exist.")
		return

	# create our dark frame averaged from all of them
	darkImage = createDarkImage(darkFrames)
	
	# Define an image to work in.
	# This will be created from the first light frame we process
	image = None
	for fileName in os.listdir(frames):
		fileName = os.path.join(frames, fileName)
		if fileIsImage(fileName):
			image = processLightFrame(fileName, image, darkImage)
	
	# show the new image if we managed to make one.
	if image == None:
		pdb.gimp_message("No images found to stack")
	else:
		gimp.Display(image)
		gimp.delete(darkImage) # we don't need this any more so get rid of it so not to leak.

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
		(PF_DIRNAME, "frames","Light Frames",""),
		(PF_DIRNAME, "dark_frames","Dark Frames","")
	],
	[],
	startrail,
	menu="<Image>/File/Create/Python-Fu",   
	domain=("gimp20-template", locale_directory) 
	)

main()
