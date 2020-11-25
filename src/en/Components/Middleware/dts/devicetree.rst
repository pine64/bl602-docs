device tree
===========

1. Introduction
---------------

- Debugging platform

   ``ubuntu18.04``

2. Convert between dts and dtb
------------------------------

- device tree debugging tool

   ``sudo sudo apt-get install device-tree-compiler``

- dts to dtb

   ``dtc -I dts -O dtb -o *.dtb *.dts``

- dtb to dts

   ``dtc -I dtb -O dts *.dtb -o *.dts``

- dtb to array to array \*.c

   ``xxd -i *.dtb ./*.c``

Three, device tree syntax format
--------------------------------

- The beginning of the \*.dts file must start with the following
   ``/dts-v1/; // version: 17 // last_comp_version: 16 // boot_cpuid_phys: 0x0``

- The hexadecimal array representation method is as follows (Note: There must be a space between bytes, and line breaks are not supported temporarily)

   ::

       mac {
               sta_mac_addr = [C8 43 57 82 73 40];
               ap_mac_addr = [C8 43 57 82 73 02];
           };

- String or string data representation method is as follows

   ::

       model = "bl bl602 AVB board";
       compatible = "bl,bl602-sample", "bl,bl602-common";

- 32bit data representation method (can use hexadecimal ox method or decimal method, there must be a space between bytes, and line breaks are not supported temporarily)

   ::

       pwr_table = <0x4 0x64>
       pwr_table = <4 100>

Four, device tree module configuration
--------------------------------------

Serial port configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    The serial port only supports the following functions for the time being

- Enable serial port

   ``status = "okay";``

- Close the serial port

   When the serial port is closed, the remaining pins, baud rate and other configurations are invalid, and the related hardware will not be initialized

   ::

       status = "disable";

- Configuration pin

   The configuration of cts and rts related functions is temporarily not supported, so for the time being, rts and cts in \``feature``\ are both \``disable``\. If string tx and rx are used, tx and rx in \ ``feature``\ need to be configured as \ ``okay``\, tx and rx in \ ``pin``\ need to select the relevant pins.

   ::

       pin {
           rx = <7>;
           tx = <16>;
       };
       feature {
           rts = "disable";
           cts = "disable";
           rx = "okay";
           tx = "okay";
       };

- Configure baud rate

   The configuration baud rate reference is as follows, the maximum support is ``2000000 bps``\ Here, ``9600``\ is taken as an example

   ::

       baudrate = <9600>;

- Configure id number

   The configuration id reference is as follows, here is \ ``<0>``\ as an example

   ::

       id = <0>;

- Configure device name

The current serial device name is /dev/ttyS\ *, as for *\ is the current serial port id number, currently the debugging port is used
   /dev/ttyS0

   ::

       pin {
               rx = <7>;
               tx = <16>;
           };
       feature {
           rts = "disable";
           cts = "disable";
           rx = "okay";
           tx = "okay";
       };
       path = "/dev/ttyS0";

