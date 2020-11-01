BL602 SDK Starter Guide
=======================

This document aims to guide users to set up a software environment for developing on the BL602 hardware.

Setting Up and Installing the SDK
---------------------------------

-  Make sure ``make`` and ``unzip`` are installed on your system.

-  Make sure you have installed software for connecting to a serial console, for example, ``Gtkterm``.

-  Decompress the SDK ``bl_iot_sdk.zip``.

Connecting to Hardware
----------------------

The related pin connections of the module are shown in the following figure. Figure 1 is the front view of the module. The number 1 is shorted with a jumper cap, the two pin headers on the left are shorted at the 2 position, and the upper two pins are connected at the 3 The pin headers are short-circuited; Figure 2 is the back view of the module. Short-circuit the two header pins `ʻIO8`` and ``LOW``.

.. figure:: imgs/image11.png
   :alt:

.. figure:: imgs/image12.png
   :alt:

Compiling and Flashing
----------------------

-  Enter your project directory, and compile using the command \ ``./genromap``

   .. figure:: imgs/image4.png
      :alt:

-  Verify the created directory named build\_out: \ ``ls build_out``

   .. figure:: imgs/image5.png
      :alt:

Downloading Binaries
--------------------

-  Enter the directory \ ``/bl_iot_sdk/tools/flash_tool``\, and run the executable ``BLFlashEnv`` .

-  Select BL602/604 as ``chip type``\ ，refer to the following picture for a sample configuration：

   .. figure:: imgs/image7.png
      :alt:

   Click\ ``download``\ . The following figure is displayed if flashing is successful:

   .. figure:: imgs/image8.png
      :alt:

After flashing is done, open the serial terminal Gtkterm with the configuration as follows：

.. figure:: imgs/image9.png
   :alt:

Make sure that \ ``DTR``\ in the lower right corner of the terminal is in black state, ``RTS`` is in gray state. ``DTR`` can be controlled by the shortcut key ``F7``, and ``RTS`` can be controlled by the shortcut key ``F8``. the final configuration is shown in the figure below.

.. figure:: imgs/image10.png
   :alt:


