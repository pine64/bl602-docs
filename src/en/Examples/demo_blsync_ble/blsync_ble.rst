.. _blsync-ble-index:

BLSYNC-BLE
==========

Overview
--------

This example mainly introduces how to use ble for wifi configuration.

APP use steps
-------------

- Compile the ``customer_app/sdk_app_ble_sync`` project and download the project firmware;
- When the firmware is powered on, it will automatically start ble broadcasting, and wait for the mobile APP to connect to the network, as shown below;

   .. figure:: imgs/image1.png
      :alt:

- Open the mobile APP to search for Bluetooth devices, and the device name "BL602-BLE-DEV" is found;

   .. figure:: imgs/image2.png
      :alt:

- After clicking to connect the device, click Scan in the APP, and after a few seconds, the APP will display the list of wifi devices scanned by the development board;

   .. figure:: imgs/image3.png
      :alt:

   .. figure:: imgs/image4.png
      :alt:

- Users can connect to the wifi that needs network configuration through the scanned device list;

   .. figure:: imgs/image5.png
      :alt:

- When the user confirms that the network configuration is completed, the network configuration function is no longer needed and can be turned off by using the "blsync_ble_stop" command.

   .. figure:: imgs/image6.png
      :alt:

Steps to use WeChat Mini Program
--------------------------------

- Compile the ``customer_app/sdk_app_ble_sync`` project and download the project firmware;
- When the firmware is powered on, it will automatically start ble broadcast, and wait for the mobile APP to connect to the network, as shown below;

   .. figure:: imgs/image1.png
      :alt:

- Open the WeChat applet to search for Bluetooth devices and find the device name "BL602-BLE-DEV";

   .. figure:: imgs/image7.png
      :alt:

- Click "BL602-BLE-DEV" to connect the device. After connecting to the BLE of the device, you will get the BLE service, click the first service, and then select "Write Notification";

   .. figure:: imgs/image8.png
      :alt:

- Click "click to configure network" in the applet, the applet will echo the obtained wifi list;

   .. figure:: imgs/image9.png
      :alt:

- Users can connect to the wifi that needs network configuration through the scanned device list, and click the name of the wifi that needs to be connected;

   .. figure:: imgs/image10.png
      :alt:

- Then enter the wifi password in the input box and click "send password" to connect to wifi;

   .. figure:: imgs/image11.png
      :alt:

- Click the "Get Status" button in the applet to get the current connection status of wifi;

   .. figure:: imgs/image12.png
      :alt:

- Currently connected to wifi, it will display "Connected" and pop up the board's IP address and other information;

   .. figure:: imgs/image13.png
      :alt:

- Click the "Disconnect wifi" button to disconnect the wifi, and click the "Get Status" button again to get the current wifi disconnected;

   .. figure:: imgs/image14.png
      :alt:

- When the user confirms that the network configuration is completed, the network configuration function is no longer needed and can be turned off by using the "blsync_ble_stop" command.

   .. figure:: imgs/image6.png
      :alt: