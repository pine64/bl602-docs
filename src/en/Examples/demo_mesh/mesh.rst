.. _demo-ble-index:

Mesh
==================

Overview
--------

This example shows how to use ble mesh.

Usage steps
-----------

- Install ``bl_mesh_app.apk`` on your phone
- Download and compile the ``customer_app/bl602_demo_event`` project
- Run following Mesh commands in the serial monitor:

   #stack_ble

   #blemesh_init

   #blemesh_pb 2 1

.. figure:: imgs/image22.png
   :align: center

- Open the app and select ADD NODE in the Network column

.. figure:: imgs/image23.png
   :align: center

- Select your device

.. figure:: imgs/image24.png
   :align: center

- Click the IDENTIFY button

.. figure:: imgs/image25.png
   :align: center

- Click the PROVISION button

.. figure:: imgs/image26.png
   :align: center

- Select No OOB in the pop-up window and click ok

.. figure:: imgs/image27.png
   :align: center

- Click ok

.. figure:: imgs/image28.png
   :align: center

- Your node is automatically added to the Network column, click on your connected device

.. figure:: imgs/image29.png
   :align: center

- Locate Elements option and click it's drop-down button

.. figure:: imgs/image30.png
   :align: center

- Select the Generic On Off Server option

.. figure:: imgs/image31.png
   :align: center

- Click the BIND KEY button

.. figure:: imgs/image32.png
   :align: center

- Click Application key 1

.. figure:: imgs/image33.png
   :align: center

- Click on the ON and OFF buttons to control the LED switch

.. figure:: imgs/image36.png
   :align: center

- The following information can be seen in the serial monitor, indicating that the LED is successfully controlled

.. figure:: imgs/image41.png
   :align: center

- Click the SUBSCRIBE button

.. figure:: imgs/image34.png
   :align: center

- Select "Create a new group to subscribe" option

.. figure:: imgs/image35.png
   :align: center

- Follow the same steps to add another node. Then click on your group

.. figure:: imgs/image37.png
   :align: center

- In the group, clicking on ON and OFF buttons prints the LED information in the serial monitor, indicating that the mesh is working

.. figure:: imgs/image38.png
   :align: center

.. figure:: imgs/image41.png
   :align: center
