.. _demo-wifi-index:

Wi-Fi
==================

Overview
--------

This demo explains Wi-Fi-relate functionalities.

Usage Steps
-----------

- Compile and flash ``customer_app/bl602_demo_wifi``.
- In the serial console, enter ``stack_wifi`` to initialize the Wi-Fi stack.

.. figure:: imgs/image1.png
   :alt:

Functionalities
---------------

- Connect to an available Wi-Fi network:

Enter the command ``wifi_sta_connect <ssid> <pwd>``, for example ``wifi_sta_connect bl_test_005 12345678``. If the connection is successful, the console will display network and available RAM information. In the picture below you can see the network's IP and mask, and the available RAM.

.. figure:: imgs/image2.png
   :alt:

- Disconnect from Wi-Fi:

Use the command ``wifi_sta_disconnect``.

.. figure:: imgs/image3.png
   :alt:

- Scan for networks:

Command ``wifi_scan``. Displays a list of networks if successful.

.. figure:: imgs/image4.png
   :alt:

- Enable AP mode:

Command: ``wifi_ap_start``. Prints out the SSID, password and channel.

.. figure:: imgs/image5.png
   :alt:

- Disable AP mode:

Command: ``wifi_ap_stop`` .

.. figure:: imgs/image6.png
   :alt:
