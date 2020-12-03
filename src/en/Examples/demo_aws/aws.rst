.. _aws-index:

AWS
===

Overview
---------

This example explains how to interact with Amazon Web Services.

Usage Steps
-----------

- Edit ``customer_app/bl602_demo_ble_pds/bl602_demo_ble_pds/aws_iot_main.c`` with your own AWS certificate and configs. This picture shows an example configuration (for demostration only):

    .. figure:: imgs/image1.png
       :alt:

- Compile and flash the ``customer_app/bl602_demo_event`` project.
- In the serial console, enter ``stack_wifi`` to start up Wi-FI，and ``wifi_sta_connect <name> <key>`` to connect to an available Wi-Fi network. Confirm that the connection is successful. (e.g.: use the command ``wifi_sta_connect bl_test_005 123456789``.)

    .. figure:: imgs/image2.png
       :alt:

    .. figure:: imgs/image3.png
       :alt:

- Enter ``aws`` in the serial console. If you see the following log printout, the connection is successful.

    .. figure:: imgs/image4.png
       :alt:
