.. _uart_ioctl-index:

UART_ioctl
==================

Overview
----------------

This example shows the modes available when using UART1.

Setup
----------------

  - See ``uart_echo``.
  - Usage
    - Connect ``gpio3``, ``gpio4``, and ``GND`` to ``TXD``, ``RXD``, and ``GND`` on a USB to TTL adapter respectively.
    - Download and compile ``customer_app/sdk_app_uart_ctl``.
    - Open one serial terminal at 115200 baud for sending and receiving UART messages, and another at 2000000 for logging. For instance, with case1, you can enter ``123456789abcdef`` in the first window, see the reply, and also print out the amount of data received to the second window.

.. figure:: imgs/image1.png
   :alt:

Examples
----------------

aos_ioctl ``IOCTL_UART_IOC_WAITRD_MODE`` and ``IOCTL_UART_IOC_WAITRDFULL_MODE``:

::

    while (1) {
        //log_info("ready to read.\r\n");
        waitr_arg.buf = buf_recv;
        waitr_arg.read_size = sizeof(buf_recv);
        waitr_arg.timeout = 0;
        res = aos_ioctl(fd, IOCTL_UART_IOC_WAITRD_MODE, (unsigned long)(&waitr_arg));
        //res = aos_ioctl(fd, IOCTL_UART_IOC_WAITRDFULL_MODE, (unsigned long)(&waitr_arg));
        if (res > 0) {
            log_info("%s name.length = %d:\r\n", name, res);
            aos_write(fd, buf_recv, res);
        }
    }

- case1: ``waitr_arg.timeout = 0`` and ``aos_ioctl(fd, IOCTL_UART_IOC_WAITRD_MODE, (unsigned long)(&waitr_arg))`` make it so that when all available data or sizeof(buf_recv) is read the length is returned immediately. ``aos_ioctl(fd, IOCTL_UART_IOC_WAITRDFULL_MODE, (unsigned long)(&waitr_arg))`` has the same usage as ``IOCTL_UART_IOC_WAITRD_MODE``.

- case2: ``waitr_arg.timeout = AOS_WAIT_FOREVER`` and ``aos_ioctl(fd, IOCTL_UART_IOC_WAITRD_MODE, (unsigned long)(&waitr_arg))`` make it so that it will wait for all available data or sizeof(buf_recv) to be read, and when there is no data available it will return immediately. ``aos_ioctl(fd, IOCTL_UART_IOC_WAITRDFULL_MODE, (unsigned long)(&waitr_arg))`` means to wait for sizeof(buf_recv) to be read and then return.

- case3: ``waitr_arg.timeout = 5000`` and ``aos_ioctl(fd, IOCTL_UART_IOC_WAITRD_MODE, (unsigned long)(&waitr_arg))`` make it so that it will wait up to 5 seconds for all available data or sizeof(buf_recv) to be read, and when there is no data available it will return immediately. ``aos_ioctl(fd, IOCTL_UART_IOC_WAITRDFULL_MODE, (unsigned long)(&waitr_arg))`` means to wait up to 5 seconds for sizeof(buf_recv) to be read and then return.

aos_ioctl ``UART_IOC_BAUD_MODE``:

::

    aos_ioctl(fd, IOCTL_UART_IOC_BAUD_MODE, 9600);

In the above, ``9600`` is the baud rate.

aos_ioctl ``IOCTL_UART_IOC_READ_BLOCK`` and ``IOCTL_UART_IOC_READ_NOBLOCK``:

::

    while (1) {
        length = aos_read(fd, buf_recv, sizeof(buf_recv));
        if (length > 0) {
            log_info("%s name.length = %d:\r\n", name, length);
            aos_write(fd, buf_recv, length);
        }
        vTaskDelay(500);
        log_info("test.\r\n");
        count++;

        if (count == 5) {
            log_info("set noblock.\r\n");
            aos_ioctl(fd, IOCTL_UART_IOC_READ_NOBLOCK, 0);
        }

        if (count == 10) {
            log_info("set block.\r\n");
            aos_ioctl(fd, IOCTL_UART_IOC_READ_BLOCK, 0);
        }
    }

``aos_ioctl(fd, IOCTL_UART_IOC_READ_BLOCK, 0)`` makes it so once sizeof(buf_recv) is read it will return, but otherwise it will wait. ``aos_ioctl(fd, IOCTL_UART_IOC_READ_NOBLOCK, 0)`` makes it so it will return once all available data or sizeof(buf_recv) is read.
