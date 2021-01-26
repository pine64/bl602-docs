.. _helloworld-index:

Hello World
===========

Overview
--------

This project explains how to start up the board and print simple logging messages to the console.

Code Examples
-------------
.. code-block:: c

    bl_uart_init(0, 16, 7, 255, 255, 230400);
    printf("Hello World!\r\n");

According to ``bl_uart_init``'s prototype:

.. code-block:: c

    int bl_uart_init(uint8_t id, uint8_t tx_pin, uint8_t rx_pin, uint8_t cts_pin, uint8_t rts_pin, uint32_t baudrate)

The ``id`` must be set to 0, other values won't work. Pine64's Nutcracker uses pin 16 for ``tx_pin`` and pin 7 for ``rx_pin``. The baud is set to 230400bps, it can be any value between 1200 (very slow) and 2000000 (very fast). The purpose of ``cts_pin`` and ``rts_pin`` remains unknown, they are not really used anywhere in the lib's code, and any value (between 0 and 255) seems to to work. Though official examples set both of them to 255.

Run the example, and you should see ``Hello World!`` printed to the serial console (screen, minicom, gtkterm...) like this:

.. code-block:: bash

    Hello World!

