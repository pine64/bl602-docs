macOS Starter Guide
===================

This document explains how to set up a macOS environment, build the ``sdk_app_helloworld`` application, flash it to the BL602 and verify the output through a serial port reader.

Installing prerequisites and cloning repository
-----------------------------------------------

The project requires the Xcode Command Line Tools, which include the ``clang`` compiler and other build tools like ``make``, to be installed. Install the tools using one of the following methods:

- Run ``xcode-select --install`` in Terminal. A dialog box will ask if you want to download and install the tools.
- `Apple Developer Downloads <https://developer.apple.com/download/all/?q=xcode>`_ offers the tools as a stand-alone dmg, which is smaller than full Xcode.
- Install `Xcode <https://apps.apple.com/us/app/xcode/id497799835>`_ from the Mac App Store. On the first run, Xcode should prompt to install the Command Line Tools.

Next, clone the SDK repository:

.. code-block:: bash

    git clone --recursive https://github.com/pine64/bl_iot_sdk

Compiling
----------------------

First, set ``BL60X_SDK_PATH`` to the location of the ``pine64/bl_iot_sdk`` repository.
Next, set ``CONFIG_CHIP_NAME`` to the make of the chip in this case ``BL602``.
If the repository is already cloned, ``pwd`` can be used to correctly set the environment variable:

.. code-block:: bash

    cd bl_iot_sdk
    export BL60X_SDK_PATH=$(pwd)
    export CONFIG_CHIP_NAME=BL602

In order to build all example projects run ``make`` in the project directory.
In order to build only a single example go to the directory of the example and run ``make``.
In order to build ``sdk_app_helloworld``:

.. code-block:: bash

    cd customer_app/sdk_app_helloworld
    make

Build artifacts will be located in the ``build_out`` folder in each example.
Change into the output of the example you want to flash and ensure that the ``.bin`` file exists:

.. code-block:: bash

    cd build_out
    ls -la *.bin

Connecting the Hardware
-----------------------

Set the jumper on ``IO8`` to cover ``IO8`` and ``H`` (the jumper should be closest to the edge of the board).

.. figure:: ../imgs/Pine64-BL602-EVB-ver-11.png
   :alt:

   Pine64 BL602 EVB ver 1.1 board. ``IO8`` jumper, ``LED2``, the ``RESET`` button and the USB-C connection have been highlighted.

Connect the board to the computer.
After connecting the board to the computer the ``RESET`` button can be used after changing the jumper setting to without repowering the device.

.. _flashing-mac:

Flashing
--------

Download the latest `blflash <https://github.com/spacemeowx2/blflash/releases>`_ version for macOS and ``chmod`` it to be executable:

.. code-block:: bash

    chmod +x blflash*

Invoke the ``blflash`` binary with the ``flash <project_name>.bin --port <port>`` arguments.

You may get an error that says that ``blflash-macos-amd64`` can't be run because macOS can't verify it's free of malware, or that the identity of the developer can't be confirmed. To fix this, control-click on the downloaded ``blflash-macos-amd64`` executable in the Finder and ``Open`` from the context menu. You should now see the same warning again, but with an ``Open`` button. After clicking ``Open`` once, the warning should be cleared and ``blflash`` commands in Terminal should run from this point on.

On macOS, the port should usually be ``/dev/tty.usbserial-1420``.
If in doubt, get a list of USB ports with ``ls -la /dev/ | grep usbserial``.

.. code-block:: bash

    ./blflash-macos-amd64 flash sdk_app_helloworld.bin --port /dev/tty.usbserial-1420

If flashing is not successful ensure that:

1. The device is connected to the computer correctly (red LED (``LED2``) should be lit).

2. The ``IO8`` jumper is correctly set to cover the ``H`` position. Press ``RESET`` to make sure the jumper change is in effect.

3. The ``sdk_app_helloworld.bin`` file exists and is correctly built at the correct location.

4. The correct port is used.

5. If attempting to flash something that is not the ``sdk_app_helloworld`` example, try flashing that first to ensure that the toolchain is working.

Alternative Flashing Tools and Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`mkroman <https://github.com/mkroman/awesome-bouffalo#rom-tools>`_ keeps a feature matrix of alternative flashing tools.

`lupyuen <https://lupyuen.github.io/articles/pinecone#other-flashing-tools>`_ has an overview of alternative tools as well as an overview of the different components of the ROM.

BouffaloLabDevCube
^^^^^^^^^^^^^^^^^^

**Note:** This section has not yet been fully tested.

Bouffalo Lab has a macOS version of their own proprietary flashing program, but it does not always seem to run reliably.
It can be found at `their official site <https://dev.bouffalolab.com/download>`_.
If a login page is reached, click the button labeled ``Dev Zone``.

Extract the ``.zip`` file and execute ``BLDevCube``.

If Dev Cube launches on your Mac, then the Linux flashing instructions for Dev Cube at :ref:`devcube-flashing-linux` should work (with the appropriate macOS port name). More information can be found at :ref:`devcube-index`.

Testing the output
------------------

Change the jumper on ``IO8`` to cover ``L`` and press the reset button.

Download `CoolTerm <https://freeware.the-meiers.org/>`_. Use CoolTerm to connect using a baud rate of ``2000000`` (two million) and the same port used in :ref:`flashing-mac`. See `lupyuen's instructions <https://lupyuen.github.io/articles/flash#watch-the-firmware-run>`_ for a screenshot of the CoolTerm configuration.

The terminal should be blank.
If you're being spammed with unknown symbols change jumper pin ``IO8`` to ``L`` and press ``RESET``.
After pressing ``RESET`` the following should be in the terminal:

.. code-block:: bash

    [helloworld]   start
    [helloworld]   helloworld
    [helloworld]   end

The above should appear on the terminal every time ``RESET`` is pressed.

Further information on the ``sdk_app_helloworld`` example can be found at :ref:`helloworld-index`.

