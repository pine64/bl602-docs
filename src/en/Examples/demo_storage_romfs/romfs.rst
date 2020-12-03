.. _romfs-index:

Romfs
=============================

Overview
-----------------------------

This example explains how to use Romfs partition.

Preparation and usage
-----------------------------

- Create a file named ``aa.bin`` inside new directory ``test/child``

.. figure:: imgs/image1.png
   :alt: 

- Usage steps：

  - When downloading, check the ``Romfs`` checkbox and specify ``test`` directory like shown in Figure 1 below. After flashing, you can use ``ls`` command to view the contents of the romfs partition;

.. figure:: imgs/image2.png
   :alt: 

.. figure:: imgs/image3.png
   :alt: 

- Use the ``romfs`` command to perform read and write operations on Romfs. You can see that the data read is consistent with the downloaded file data.

.. figure:: imgs/image4.png
   :alt: 

.. figure:: imgs/image5.png
   :alt: 

Operations
-----------------------------

- Opening a file:

::
    
    fd = aos_open("/romfs/demo.bin", 0);
    log_info("fd = %d\r\n", fd);
    if (fd < 0) {
        log_error("open error.\r\n");
        return;
    }
 
- Reading file contents:

::

    len = aos_read(fd, buf, 1);
    log_info("len = %d\r\n", len);
    log_buf(buf, 1);

- Seeking：

::
    
    aos_lseek(fd, 1, SEEK_CUR);
    memset(buf, 0, sizeof(buf));
    len = aos_read(fd, buf, 1);
    log_info("len = %d\r\n", len);
    log_buf(buf, 1);

- Getting the file address and file size:

::

    aos_ioctl(fd, IOCTL_ROMFS_GET_FILEBUF, (long unsigned int)&filebuf);
    log_info("filebuf.buf = %p\r\n", filebuf.buf);
    log_info("filebuf.bufsize = %lu\r\n", filebuf.bufsize);


