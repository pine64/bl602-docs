.. _httpc-index:

Httpc client
==================

Overview
--------

This example explains the process of how to access the Http server to obtain data through tcp.

Usage Steps
----------------

- Prepare a usable URL and network.

- Steps to use:

  - Enter the command ``stack_wifi`` to turn on wifi in the terminal, then enter the command ``wifi_sta_connect <name> <key>`` to connect to wifi. Confirm that the wifi connection is successful (e.g.: use the command ``wifi_sta_connect bl_test_005 12345678``).

    .. figure:: imgs/image1.png
       :alt:

    .. figure:: imgs/image2.png
       :alt:

  - Use the ``httpc`` command to download.

    .. figure:: imgs/image3.png
       :alt:

Applications
------------

- Main process

::

    settings.use_proxy = 0;
    settings.result_fn = cb_httpc_result;
    settings.headers_done_fn = cb_httpc_headers_done_fn;
    httpc_get_file_dns(
            "nf.cr.dandanman.com",
            80,
            "/ddm/ContentResource/music/204.mp3",
            &settings,
            cb_altcp_recv_fn,
            &req,
            &req
   );

``cb_httpc_result()`` will be called after the http transmission is finished to print the length of the message content. ``cb_httpc_headers_done_fn()`` will be called when the http headers are received, and the size of the headers will be printed. The user can process the received message in ``cb_altcp_recv_fn()``.
