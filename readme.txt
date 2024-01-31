

this is a mess of the code and tools I made for Resident Evil Kart.

A rom of Super Mario Kart (unheadered) labeled "Super Mario Kart (U).sfc" needs to be provided in this folder for the build step to work.

Tools to edit the cameras are in the tools folder.
To change the track, open tools/CAM_TOOL.py and change the line "MAP_NUM = MAP_MC1" to indicate which map you want to edit. The list is above that line in the code.

In Camera editing mode, left click on a camera to pick it up and move it around. 
While holing the camera, scroll to rotate the camera, or press right click to delete that camera.
Left click again to place the camera back down.
While not holding a camera, right click to create a new camera.

Press C to swap between Camera editing mode and Zone editing mode, and vice versa.

In Zone editing mode, left click on a camera to select it, and then right click on a zone to bind that zone to the selected camera.
By left clicking on a zone, the camera it is attached to will also be selected, and all of the zones attached to the camera will be highlighted.

Press S to save changes to the json file.

To apply changes to the zones.asm file, save your changes, and then run "cnv_cam_json_to_tables.py", 
and then you can build the ROM with BUILD.bat to save the cameras.

Do not use "cnv_asm_to_json.py" unless you know *exactly* what you are doing. This will overwrite your current camera settings to the last build version,
and will overwrite any changes you didnt apply to the asm file.

Do not edit the zones.asm file with any other means than with the "cnv_cam_json_to_tables.py" file, your changes will be overwritten.


Happy Karting,
  -MrL




