Linux Starter Guide
===================

This document explains how to set up a software environment for developing on the BL602 hardware under Linux.

Setting Up and Installing the SDK
---------------------------------

-  Make sure ``make`` and ``unzip`` are installed on your system.

-  Make sure you have installed software for connecting to a serial console, for example, ``Gtkterm``.

-  Decompress the SDK ``bl_iot_sdk.zip``.

Connecting to Hardware
----------------------

This picture shows the front of the module. Connect the pins in position 1, 2 and 3 with jumper caps.


.. figure:: imgs/image1110.png
   :alt:
   
This picture shows the back of the module. Connect the header pin `ʻIO8`` to ``LOW``.

.. figure:: imgs/image127.png
   :alt:

Compiling and Flashing
----------------------

-  Enter your project directory, and compile using the binary \ ``./genromap``

   .. figure:: imgs/image48.png
      :alt:

-  Verify the created directory named build\_out: \ ``ls build_out``

   .. figure:: imgs/image57.png
      :alt:

Downloading Binaries
--------------------

-  Run the executable ``BLFlashEnv`` \ under the folder ``/bl_iot_sdk/tools/flash_tool``\.

-  Select BL602/604 as ``chip type``\ ，and configure the rest as follows：

   .. figure:: imgs/image72.png
      :alt:

   Click\ ``download``\ . You should see the following if flashing is successful:

   .. figure:: imgs/image82.png
      :alt:

After flashing is done, use a serial terminal (e.g. Gtkterm) and connect to the module:

.. figure:: imgs/image92.png
   :alt:

Make sure to enable ``DTR`` and disable ``RTS`` . In Gtkterm, you can toggle ``DTR`` with the shortcut key ``F7``, and ``RTS`` with the shortcut key ``F8``. See following for an example:

.. figure:: imgs/image102.png
   :alt:


