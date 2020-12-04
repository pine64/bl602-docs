.. _gpio-index:

GPIO
==================

Overview
-----------------------------

This example explains how to configure GPIO.

Usage Steps
-----------

- Compile and flash ``customer_app/sdk_app_gpio``.
- In the serial console, use ``gpio-func <pinnum> <inputmode> <pullup> <pulldown>`` to configure a GPIO pin. ``input_mode`` configures whether the pin is an input (and otherwise, an output), and ``pullup`` and ``pulldown`` respectively configures the pull-up and pull-down states. For instance, ``gpio-func 8 0 0 0`` configures gpio pin 8 as output without pull-up / pull-down.

.. figure:: imgs/image1.png
   :alt:

- Use ``gpio-set <pinnum> <val>`` to configure the voltage level of a pin (an output pin).

.. figure:: imgs/image2.png
   :alt:

- Use ``gpio-get <pinnum>`` to look up the voltage level of a pin.

.. figure:: imgs/image3.png
   :alt:


Code Examples
-------------

- Implementation of ``gpio-func``

::

    if (5 != argc) {
        printf("Usage: %s 24 1 1 0\r\n  set GPIO24 to input with pullup\r\n",
                argv[0]
        );
        return;
    }
    ionum = atoi(argv[1]);
    inputmode = atoi(argv[2]);
    pullup = atoi(argv[3]);
    pulldown = atoi(argv[4]);
    if (ionum < 0 || inputmode < 0 || pullup < 0 || pulldown < 0) {
        puts("Illegal arg\r\n");
        return;
    }
    printf("GPIO%d is set %s with %s pullup %s pulldown\r\n",
            ionum,
            inputmode ? "input" : "output",
            pullup ? "Active" : "null",
            pulldown ? "Active" : "null"
    );
    if (inputmode) {
        bl_gpio_enable_input(ionum, pullup ? 1 : 0, pulldown ? 1 : 0);
    } else {
        bl_gpio_enable_output(ionum, pullup ? 1 : 0, pulldown ? 1 : 0);
    }

It receives inputs from the serial console, and pass them as parameters to ``bl_gpio_enable_input(uint8, uint8, uint8)`` or ``bl_gpio_enable_output(uint8, uint8, uint8)`` to configure the corresponding GPIO pin.

- Implementation of ``gpio-set``

::

    if (3 != argc) {
        printf("Usage: %s 24 1\r\n  set GPIO24 output to high\r\n",
                argv[0]
        );
        return;
    }
    ionum = atoi(argv[1]);
    val = atoi(argv[2]);
    if (ionum < 0 || val < 0) {
        puts("Illegal arg\r\n");
        return;
    }
    printf("GPIO%d is set to %s\r\n",
        ionum,
        val ? "high" : "lo"
    );
    bl_gpio_output_set(ionum, val ? 1 : 0);

It receives inputs from the CLI and pass them to ``bl_gpio_output_set(uint8, uint8)``.

- Implementation of ``gpio-get``

::

   if (2 != argc) {
        printf("Usage: %s 24\r\n  get GPIO24 value\r\n",
                argv[0]
        );
        return;
    }
    ionum = atoi(argv[1]);
    if (ionum < 0) {
        puts("Illegal arg\r\n");
        return;
    }
    ret = bl_gpio_input_get(ionum, &val);
    printf("GPIO%d val is %s\r\n",
        ionum,
        0 == ret ? (val ? "high" : "low") : "Err"
    );

It receives inputs from the CLI and pass them to ``bl_gpio_input_get(uint8, uint8*)``

- In ``customer_app/sdk_app_gpio/sdk_app_gpio/main.c``, the function ``static void _cli_init()`` invokes ``gpio_cli_init()`` to initialize GPIO-related commands.
