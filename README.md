# LISA
Museum videoguide for deaf visitors


LISA was born from the idea of enabling deaf museum visitors to easily enjoy the insights provided to hearing visitors through audio guides. To do so, LISA reproduces videos of a guide speaking in sign languages.


Hardware Requirements:

    • Raspberry Pi 4;
    • SD card;
    • Coral Edge TPU USB accelerator;
    • Raspberry Pi Camera (https://www.az-delivery.de/it/products/raspberrykamerav1-3?variant=27479410505);
    • 3.5" LCD Display (https://www.waveshare.com/3.5inch-rpi-lcd-b.htm);
    • 3A Power Bank;

To set up LISA, follow these steps:

    • Download the entire LISA folder;
    • Create the PCB following the "Guides/homemade-pcb-guide.pdf";
    • Connect both the Pi Camera and the PCB to the Raspberry Pi while it is powered off;
    • Connect the Button Hub with jumper wires;
    • Connect the Coral accelerator;
    • Install all the necessary dependencies following the "Guides/dependencies-guide.pdf";
    • Follow the steps in the "Guides/compatibility-display-cam-guide.pdf" to make the display and camera work simultaneously;
    • If you want LISA to run at startup, follow the "Guides/run-at-start-guide.pdf", otherwise manually run "Detector/lisa.py".
