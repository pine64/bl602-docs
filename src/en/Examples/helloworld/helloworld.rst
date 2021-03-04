.. _helloworld-index:

Hello World
===========

Overview
--------

This project explains how to start up the board and print simple logging messages to the console.

Code Examples
-------------
::

    bl_uart_init(0, 16, 7, 255, 255, 2 * 1000 * 1000);
    helloworld();

Here we configure the baud rate to 2000000bps. Run the example, and you should see ``start`` ， ``helloworld`` ， ``end`` printed to the serial console.

.. code-block:: bash

    [helloworld]   start
    [helloworld]   helloworld
    [helloworld]   end

