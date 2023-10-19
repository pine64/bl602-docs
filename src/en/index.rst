.. user manual documentation master file, created by
   sphinx-quickstart on Wed Jul  3 15:54:19 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Home
====

The `BL602 <https://www.bouffalolab.com/bl602>`_ is a general purpose microcontroller based on the "SiFive E24 Core" RISC-V processor with provisions for 2.4 GHz Wi-Fi and Bluetooth Low Energy 5.0.
It is intended to be used in `IoT <https://en.wikipedia.org/wiki/Internet_of_things>`_ and other ultra-low-power applications.
The microcontroller supports flashing and communication over `UART <https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter>`_, and flashing, communication, and debugging over `JTAG <https://en.wikipedia.org/wiki/JTAG>`_.

.. toctree::
   :caption: Quick Start Guide
   :numbered:

   Quickstart_Guide/get_started
   Quickstart_Guide/Linux/Quickstart_Linux_ubuntu
   Quickstart_Guide/Windows/Quickstart_Windows_msys
   Quickstart_Guide/Windows/Quickstart_Windows_wsl
   Quickstart_Guide/Mac/Quickstart_macOS
   Quickstart_Guide/connecting_the_hardware

.. toctree::
   :caption: Developer Environment
   :numbered:

   Developer_Environment/Setting_Up
   Developer_Environment/BLFlashEnv/BLFlashEnv
   Developer_Environment/freedom_studio/freedom_studio
   Developer_Environment/eclipse/eclipse

.. toctree::
   :caption: Examples
   :numbered:

   Examples/README
   Examples/helloworld/helloworld
   Examples/demo_aws/aws
   Examples/demo_at/AT
   Examples/demo_audio_udp/audio_udp
   Examples/demo_ble/ble
   Examples/demo_blsync_ble/blsync_ble
   Examples/demo_cronalarm/cronalarm
   Examples/demo_dac/DAC
   Examples/demo_hbnram/hbnram
   Examples/demo_mesh/mesh
   Examples/demo_peripherals_gpio/GPIO
   Examples/demo_peripherals_uart_echo/uart_echo
   Examples/demo_peripherals_uart_ioctl/uart_ioctl
   Examples/demo_protocols_http/http
   Examples/demo_protocols_httpc/httpc
   Examples/demo_storage_psm/psm
   Examples/demo_storage_romfs/romfs
   Examples/demo_system_cli/cli
   Examples/demo_system_fdt/fdt
   Examples/demo_wifi/wifi
   Examples/demo_zb/zigbee
   Examples/sdk_app_easyflash_boottimes/easyflash_boottimes
   Examples/sdk_app_pwm/pwm
   Examples/benchmark_security_aes/benchmark_security_aes_gcm

.. toctree::
   :caption: Components
   :numbered:

   Components/Command_line/helper
   Components/Command_line/aos_cli
   Components/Middleware/dts/devicetree
   Components/Middleware/log/blog
   Components/Middleware/vfs/vfs
   Components/Middleware/yloop/yloop
   Components/Network/wifi/wifi
   Components/BLE/ble_stack/ble_stack

.. toctree::
   :caption: API
   :numbered:

   API/sys/cronalarms
   API/wifi/wifi_mgmr

.. toctree::
   :caption: Documentation
   :numbered:

   README/README

