.. _http-index:

Http client
==================

Overview
------

This example explains the process of how to create a socket and connect to access the specified Http server to obtain data.

Preparation and Usage Steps
----------------

- Prepare a usable URL and network.

- Steps to use:
   
  - Compile and flash ``customer_app/sdk_app_http_client_socket``.
  - Enter the command ``stack_wifi`` to turn on wifi in the terminal, then enter the command ``wifi_sta_connect <name> <key>`` to connect to wifi. Confirm that the wifi connection is successful (e.g. use the command ``wifi_sta_connect bl_test_005 12345678``).

    .. figure:: imgs/image1.png
       :alt: 

    .. figure:: imgs/image2.png
       :alt: 


  - Use ``http`` command to download through socket.

    .. figure:: imgs/image3.png
       :alt: 


Applications
---------

- Obtain ``hostinfo`` by ``hostname``.

::

    struct hostent *hostinfo = gethostbyname(hostname);
    if (!hostinfo) {
        printf("gethostbyname Failed\r\n");
        return -1;
    }
  
- Create a ``socket`` connection and send the http request.

::

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("Error in socket\r\n");
        return -1;
    }
    /*---Initialize server address/port struct---*/
    memset(&dest, 0, sizeof(dest));
    dest.sin_family = AF_INET;
    dest.sin_port = htons(PORT);
    dest.sin_addr = *((struct in_addr *) hostinfo->h_addr);
    //char ip[16];
    uint32_t address = dest.sin_addr.s_addr;
    char *ip = inet_ntoa(address);

    printf("Server ip Address : %s\r\n", ip);
    /*---Connect to server---*/
    if (connect(sockfd,
             (struct sockaddr *)&dest,
             sizeof(dest)) != 0) {
        printf("Error in connect\r\n");
        return -1;
    }
    /*---Get "Hello?"---*/
    memset(buffer, 0, MAXBUF);
    char wbuf[]
        = "GET /ddm/ContentResource/music/204.mp3 HTTP/1.1\r\nHost: nf.cr.dandanman.com\r\nUser-Agent: wmsdk\r\nAccept: */*\r\n\r\n";
    write(sockfd, wbuf, sizeof(wbuf) - 1);

- Recieve http response data. Print the time of cost to recieve data and the speed of transfer when complete.

::

    while (1) {
        ret = read(sockfd, recv_buffer, BUFFER_SIZE);
        if (ret == 0) {
            printf("eof\n\r");
            break;
        } else if (ret < 0) {
            printf("ret = %d, err = %d\n\r", ret, errno);
            break;
        } else {
            total += ret;
            /*use less debug*/
            if (0 == ((debug_counter++) & 0xFF)) {
                printf("total = %d, ret = %d\n\r", total, ret);
            }
            //vTaskDelay(2);
            if (total > 82050000) {
                ticks_end = xTaskGetTickCount();
                time_consumed = ((uint32_t)(((int32_t)ticks_end) - ((int32_t)ticks_start))) / 1000;
                printf("Download comlete, total time %u s, speed %u Kbps\r\n",
                        (unsigned int)time_consumed,
                        (unsigned int)(total / time_consumed * 8 / 1000)
                );
                break;
            }
        }

- Close ``socket``.

:: 

    close(sockfd);

- In ``customer_app/sdk_app_http_client_socket/sdk_app_http_client_socket/demo.c``, the function ``static void _cli_init()`` would call ``http_client_cli_init()`` to initialize http.
