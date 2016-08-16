##1.8
* Add Skyglow removal option.
##1.7
* Updated documentation to be more clear.
##1.6
* New feature: User can opt to have progress displayed to screen at the expense of a slower processing speed.
* New feature: Once process is complete the user is notified of how long this took in seconds. Note: On occasions this prompt appears behind the main GIMP window, this appears to be a GIMP bug as it only occurs in 2.8, works as expecting in 2.9 development build of GIMP.
* Minor code clear up.

##1.5
* Corrected issue with dark frame handling.

##1.4
* Fixed issue #4 - Intermediate save path is not checked for existence.
* Fixed issue #5 - Refactor of base code.
* Various minor tweaks.

##1.3
* Added new option to save the intermediate frames after each layer is added.
* Fixed issue #2 (Dark frame opacity wrong).

##1.2
* Removed need to specify width and height, now worked out using the 1st frame.
* Corrected handling of dark frames.  Dark frames are 1st averaged into a single dark image this is then differenced from each light frame prior to layering via lighten.

##1.1
* Removed need to specify the file extension of the frames.
* General tidy up of code.

##1.0
* Initial Release.
