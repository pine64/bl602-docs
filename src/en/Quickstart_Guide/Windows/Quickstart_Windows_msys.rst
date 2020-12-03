Windows Starter Guide
=======================

This document explains how to set up a software environment for developing on the BL602 hardware under Windows.


Setting up the build environment and getting the code
-----------------------------------------------------

-   Install a serial port tool such as `ScriptCommunicator <https://gigenet.dl.sourceforge.net/project/scriptcommunicator/Windows/ScriptCommunicatorSetup_05_10_windows.zip>`__

-  `Obtain the MSYS2 installer <https://sourceforge.net/projects/msys2/files/Base/x86_64/>`__

-  `Installation instructions <https://www.msys2.org/>`__

-  Open MSYS2 and install make，by using the command：\ ``pacman -S make``

   .. figure:: imgs/image1.png
      :alt:

   .. figure:: imgs/image2.png
      :alt:

-  Open the installation directory of MSYS2 and put the SDK source code under the user name folder in the \ ``home''\ directory. The following figure shows the \ ``igor``\ folder

   .. figure:: imgs/image3.png
      :alt:

   **Note**\ ：In the example the name ``igor`` is used, but yours is probably different, you can find it by seeing what is before the @ symbol in the prompt.

-  Install unzip in order to decompress the SDK, by using the command：\ ``pacman -S unzip``\ ，You may also want git and tmux, you can install them by using these commands：\ ``pacman -S git``\ , \ ``pacman -S tmux``

   .. figure:: imgs/image4.png
      :alt:

   .. figure:: imgs/image5.png
      :alt:

-  Decompress the zip file containing the SDK, by running the command: ``unzip bl_iot_sdk.zip``

   .. figure:: imgs/image6.png
      :alt:


Connecting to Hardware
----------------------

This picture shows the front of the module. Connect the pins in position 1, 2 and 3 with jumper caps.

.. figure:: imgs/image13.png
   :alt:

This picture shows the back of the module. Connect the header pin IO8 to LOW.


.. figure:: imgs/image14.png
   :alt:

Compiling and Flashing
----------------------

-  Enter the directory of the project you want to compile, such as：\ ``cd customer_app/bl602_demo_event``

   .. figure:: imgs/image7.png
      :alt:

-  To compile run the command：\ ``./genromap``

   .. figure:: imgs/image8.png
      :alt:

Downloading Binaries
--------------------

-  Open ``bl_iot_sdk/tools/flash_tool`` and run the ``simple_flasher.exe`` program

-  For ``chip type``\ select\ ``BL602/604``\：

   .. figure:: imgs/image9.png
      :alt:

   Click ``download``. You should see the following if flashing is successful:

   .. figure:: imgs/image10.png
      :alt:

-  If you are using ScriptCommunicator, Open it and click ``settings`` to configure as shown in the figure below, where ``DTR`` needs to be checked, and ``RTS`` is not checked.

   .. figure:: imgs/image12.png
      :alt:

(You can also do this using Windows Subsystem for Linux)
