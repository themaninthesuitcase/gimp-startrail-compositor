1.3
===============
Added new option to save the intermediate frames after each layer is added.
Fixed issue #2 (Dark frame opacity wrong).

1.2
===============
Removed need to specify width and height, now worked out using the 1st frame.
Corrected handling of dark frames.  Dark frames are 1st averaged into a single dark image this is then differenced from each light frame prior to layering via lighten.

1.1
===============
Removed need to specify the file extension of the frames
General tidy up of code

1.0
===============
Initial Release