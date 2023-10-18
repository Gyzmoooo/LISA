# LISA
Museum videoguide for deaf visitors


LISA was born from the idea of enabling deaf museum visitors to easily enjoy the insights provided to hearing visitors through audio guides. To do so, LISA reproduces videos of a guide speaking in sign languages.


Hardware requirements:

    • Raspberry Pi 4;
    • SD card;
    • Coral Edge TPU USB accelerator;
    • Raspberry Pi Camera (https://www.az-delivery.de/it/products/raspberrykamerav1-3?variant=27479410505);
    • Display LCD 3.5" (https://www.waveshare.com/3.5inch-rpi-lcd-b.htm);
    • Power Bank 3A;

In order to make LISA follow these steps:

    • Download the whole LISA folder;
    • Create the PCB following the "Guides/homemade-pcb-guide.pdf";
    • Connect both the Pi Camera and the PCB on the Raspberry PI while it is powered off;
    • Connect the Button Hub with jumper wires;
    • Connect the Coral;
    • Install all the necessary dependencies following the "Guides/dependencies-guide.pdf";
    • Follow the steps in the "Guides/compatibility-display-cam-guide.pdf" to make the display and camera work simultaneously;
    • If you want to run it at the start follow the "Guides/run-at-start-guide.pdf", else just run the "Detector/lisa.py" manually;
