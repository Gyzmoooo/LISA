HOW TO ENSURE PROPER FUNCTIONALITY OF BOTH THE DISPLAY
AND THE CAMERA
To ensure proper functionality of both the display and the camera when connected simultaneously,
follow these steps:
1. Connect both the display and the camera while the Raspberry Pi is powered off;
2. Download both the 'original-directory' and 'modified-directory';
3. Navigate to the original directory and make 'LCD-hdmi' and 'LCD35-show' executable using
the following commands:
- chmod 755 <fileName> / chmod u+x <fileName>
4. Execute 'LCD-show' by running the command:
- ./LCD-show
5. Reboot your Raspberry Pi; you should now see your desktop on the display;
6. Return to the original directory and execute 'LCD-hdmi' using the command:
- ./LCD-hdmi
7. Reboot your Raspberry Pi;
8. Navigate to the modified directory and make 'hdmi' and 'show' executable by typing:
- chmod 755 <fileName> / chmod u+x <fileName>
9. If you wish to use the display and the camera, go to the modified folder and execute 'show'
by typing:
- ./show
10. To revert back to the monitor, execute 'hdmi' by typing:
- ./hdmi
