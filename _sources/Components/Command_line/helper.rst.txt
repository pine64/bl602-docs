helper
======

Here are lists of currently available commands, including system commands and user commands. Some of the command might not be well supported at moment, run ``help`` to see what commands are supported at moment, for extra commands please either refer to the source code or add by yourself.

cli list
----------

-  **System commands**

+-----------+---------------------+
| name      | help                |
+===========+=====================+
| help      | print this          |
+-----------+---------------------+
| p         | print memory        |
+-----------+---------------------+
| m         | modify memory       |
+-----------+---------------------+
| cho       | echo for command    |
+-----------+---------------------+
| xit       | close CLI           |
+-----------+---------------------+
| evname    | print device name   |
+-----------+---------------------+
| ysver     | system version      |
+-----------+---------------------+
| eboot     | reboot system       |
+-----------+---------------------+
| oweroff   | poweroff system     |
+-----------+---------------------+
| ime       | system time         |
+-----------+---------------------+
| ta        | system ota          |
+-----------+---------------------+
| s         | thread dump         |
+-----------+---------------------+

-  **User command**

+-------------------------+-----------------------------------------------------+
| name                    | help                                                |
+=========================+=====================================================+
| test\_trng              | Test TRNG                                           |
+-------------------------+-----------------------------------------------------+
| tcpc                    | create a tcpc for in a new task                     |
+-------------------------+-----------------------------------------------------+
| ipc                     | iperf TCP client                                    |
+-------------------------+-----------------------------------------------------+
| ips                     | iperf TCP server                                    |
+-------------------------+-----------------------------------------------------+
| ipu                     | iperf UDP client                                    |
+-------------------------+-----------------------------------------------------+
| psm\_set                | psm set                                             |
+-------------------------+-----------------------------------------------------+
| psm\_unset              | psm unset                                           |
+-------------------------+-----------------------------------------------------+
| psm\_get                | psm get                                             |
+-------------------------+-----------------------------------------------------+
| psm\_dump               | psm dump                                            |
+-------------------------+-----------------------------------------------------+
| psm\_erase              | psm dump                                            |
+-------------------------+-----------------------------------------------------+
| amr                     | amr encode test                                     |
+-------------------------+-----------------------------------------------------+
| test\_sdh               | test SDH based on fatfs                             |
+-------------------------+-----------------------------------------------------+
| http                    | http client download test                           |
+-------------------------+-----------------------------------------------------+
| mjpeg\_start            | start mjpeg tasks                                   |
+-------------------------+-----------------------------------------------------+
| msg\_set                | message set                                         |
+-------------------------+-----------------------------------------------------+
| msg\_get                | message get                                         |
+-------------------------+-----------------------------------------------------+
| msg\_dump               | message dump                                        |
+-------------------------+-----------------------------------------------------+
| msg\_reset              | erase all message regions                           |
+-------------------------+-----------------------------------------------------+
| msg\_set\_t1            | message set test 1                                  |
+-------------------------+-----------------------------------------------------+
| rf\_dump                | rf dump                                             |
+-------------------------+-----------------------------------------------------+
| wifi\_ap\_start         | start AP mode                                       |
+-------------------------+-----------------------------------------------------+
| wifi\_scan              | wifi scan                                           |
+-------------------------+-----------------------------------------------------+
| wifi\_mon               | wifi monitor                                        |
+-------------------------+-----------------------------------------------------+
| wifi\_raw\_send: wifi   | raw send test                                       |
+-------------------------+-----------------------------------------------------+
| wifi\_sta\_disconnect   | wifi station disconnect                             |
+-------------------------+-----------------------------------------------------+
| wifi\_sta\_connect      | wifi station connect                                |
+-------------------------+-----------------------------------------------------+
| airkiss                 | airkiss                                             |
+-------------------------+-----------------------------------------------------+
| rc\_fix\_en             | wifi rate control fixed rate enable                 |
+-------------------------+-----------------------------------------------------+
| rc\_fix\_dis            | wifi rate control fixed rate diable                 |
+-------------------------+-----------------------------------------------------+
| wifi\_capcode           | capcode utils, wifi\_capcode [cap\_in] [cap\_out]   |
+-------------------------+-----------------------------------------------------+
| blfdt                   | blfdt                                               |
+-------------------------+-----------------------------------------------------+
| tc\_uart                | bl test uart                                        |
+-------------------------+-----------------------------------------------------+
| audio\_play\_ram        | play sound fm ram                                   |
+-------------------------+-----------------------------------------------------+
| audio\_config\_es8311   | config ES831                                        |
+-------------------------+-----------------------------------------------------+
| audio\_mp3              | play sou mp3                                        |
+-------------------------+-----------------------------------------------------+
| audio\_test             | play test                                           |
+-------------------------+-----------------------------------------------------+
| audio\_play             | audio play                                          |
+-------------------------+-----------------------------------------------------+

Common commands
---------------

-  **View all commands**

   Press ``TAB`` or type ``help`` to view:

   **#** ``help``

-  **Config wifi with specified ssid and passwd(default value will be used after reboot)**

   Example: use SSID: ``bl_wifi_005`` and password: ``123456789``

   **#** ``wifi_sta_connect bl_wifi_005 123456789``

-  **Set default ssid and passwd for wifi**

   Example: use SSID: ``bl_wifi_005`` and password: ``123456789``

   **#** ``psm_set conf_ap_ssid bl_wifi_005``

   **#** ``psm_set conf_ap_psk 123456789``

-  **Start AP**

   Use ``wifi_ap_start`` to start AP，you have to run ``psm_erase`` to erase STA related config
   information and reboot. The default AP SSID is ``BL60X_uAP_`` suffixed with HEX code of the
   last 3 bytes of MAC address, the password will be ``bouffalolab``

-  **Reboot system**

   **#** ``reboot``

-  **Audio recoding and playing**

   This module requires SD support, and it only supports pcm format at moment

   -  config sample rate

      **#** audio\_config 11p025

      If no parameter is provided, a default of 16Khz will be used, the supported
      sample rates are:
      8k, 16k, 24k, 32k, 48k, 11p025, 22p05, 44p1
      Sample rate with decimal is represented with ``p`` as decimal point.
      ex, 11.025khz is represented as 11p025

   -  recoding

      **#** audio\_record test.pcm

      If no parameter is provided, a default ``record.pcm`` will be saved under the root of SD card.
	  The default recording time will be 10s

   -  playing

      **#** audio\_play test.pcm

      If no parameter is provided, it will try to plya ``record.pcm`` under the root of SD card.

-  **Image transfer**

   Use ``mjpeg_start`` command to start image transfer related tasks.

-  **Save image to SD card**

   This module requires SD support, and it only supports jpeg format at moment

   -  config quality of mjpeg images

      **#** mjpegsd\_config 50

      currently support 6 quality settings: 5, 10, 25, 50, 75, 100

   -  Start to save images

      **#** mjpegsd\_start

      default to save stream at 50FPS

   -  **NOTE**

      -  the command above will save 50 images files under SD root as:
         0.jpeg, 1.jpeg, ..., 49.jpeg

-  **Save AVI to SD card**

   This module requires SD support, and it only supports AVI format at moment

   -  config quality of mjpeg images

      **#** avisd\_config 50 bl\_avi\_q50.avi

      currently support 6 quality settings: 5, 10, 25, 50, 75, 100

   -  Start saving avi

      **#** avisd\_start

      Default to save at 750FPS

   -  **NOTE**

      -  the command above will create a file called "bl\_avi\_q50.avi" under SD root

      -  it is recommanded to set the allocation unit size to be "64KB", and filesystem to be FAT32 while formatting

      -  a reboot is needed if quality has to be modified after ``avisd\_start``

      -  psram, camera are needed for this module.

-  **Share WIFI through QR code**

   This module enables a connection to WIFI throuhg QR code

   -  start

      ``qrcode_connect_wifi``

      the camera will initilize and scan for QR code

   -  **NOTE**

      -  QR code information will be printed out once it has been recoginized, if it is not a valid WIFI hotspot, the
	     module will carry on with QR scanning

      -  Support UTF-8 encoded Chinese SSID

      -  Support open WIFI

      -  psram, camera are needed for this module.
