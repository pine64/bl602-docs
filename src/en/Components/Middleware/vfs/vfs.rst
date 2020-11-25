AOS VFS
=======

- `Summary`

- `Standard interface provided by VFS`

- `VFS data structure`

- `Take aos\_open as an example to introduce its file opening method`

- `Load the driver file or file system into the VFS`

- `Sample Code`

- `Notes`


Summary
-------

The meaning of VFS, shields the difference of the underlying file system, and provides a standard system call interface for the application layer.

Standard interface provided by VFS
----------------------------------

The basic common UNIX interfaces have been implemented. It has the prefix ``aos_``\. Because these are external interfaces, in AliOS.
The code naming rules of Things stipulate: All external interfaces need to be prefixed with \ ``aos_``

aos\_open

aos\_close

aos\_read

aos\_write

aos\_ioctl

aos\_poll

aos\_fcnt

aos\_lseek

aos\_sync

aos\_stat

aos\_unlink

aos\_rename

aos\_opendir

aos\_closedir

aos\_readdir

aos\_mkdir

VFS data structure
------------------

``inode_t``\data structure

.. code:: c

    /* this structure represents inode for driver and fs*/
    typedef struct {
        union inode_ops_t ops; /* inode operations */
        void *i_arg; /* per inode private data */
        char *i_name; /* name of inode */
        int i_flags; /* flags for inode */
        uint8_t type; /* type for inode */
        uint8_t refs; /* refs for inode */
    } inode_t;

Because the VFS virtual file system treats files and directories as files, the above data structure is an index node type, which has the operation method of the node, the data storage pointer of the node, and the name of the node (that is, the node path name/dev/null ), node type, number of times the node is referenced.

In the \ ``inode_``\ t structure, ops is the operation method for index nodes, as follows:

.. code:: c

    union inode_ops_t {

        const file_ops_t *i_ops; /* char driver operations */

        const fs_ops_t *i_fops; /* FS operations */

    };
    typedef const struct file_ops file_ops_t; /* Operation method for files */
    typedef const struct fs_ops fs_ops_t; /* Operation method for directories */
    struct file_ops {
        int (*open) (inode_t *node, file_t *fp);
        int (*close) (file_t *fp);
        ssize_t (*read) (file_t *fp, void *buf, size_t nbytes);
        ssize_t (*write) (file_t *fp, const void *buf, size_t nbytes);
        int (*ioctl) (file_t *fp, int cmd, unsigned long arg);
    #ifdef AOS_CONFIG_VFS_POLL_SUPPORT
        int (*poll) (file_t *fp, bool flag, poll_notify_t notify, struct pollfd *fd, void *arg);
    #endif
    };
    struct fs_ops {
        int (*open) (file_t *fp, const char *path, int flags);
        int (*close) (file_t *fp);
        ssize_t (*read) (file_t *fp, char *buf, size_t len);
        ssize_t (*write) (file_t *fp, const char *buf, size_t len);
        off_t (*lseek) (file_t *fp, off_t off, int whence);
        int (*sync) (file_t *fp);
        int (*stat) (file_t *fp, const char *path, struct stat *st);
        int (*unlink) (file_t *fp, const char *path);
        int (*rename) (file_t *fp, const char *oldpath, const char *newpath);
        aos_dir_t *(*opendir) (file_t *fp, const char *path);
        aos_dirent_t *(*readdir) (file_t *fp, aos_dir_t *dir);
        int (*closedir) (file_t *fp, aos_dir_t *dir);
        int (*mkdir) (file_t *fp, const char *path);
        int (*rmdir) (file_t *fp, const char *path);
        void (*rewinddir)(file_t *fp, aos_dir_t *dir);
        long (*telldir) (file_t *fp, aos_dir_t *dir);
        void (*seekdir) (file_t *fp, aos_dir_t *dir, long loc);
        int (*ioctl) (file_t *fp, int cmd, unsigned long arg);
        int (*statfs) (file_t *fp, const char *path, struct statfs *suf);
        int (*access) (file_t *fp, const char *path, int amode);
    };

``file_t``\ data structure

.. code:: c

    typedef struct {
        inode_t *node; /* node for file */
        void *f_arg; /* f_arg for file */
        size_t offset; /* offset for file */
    } file_t;

The above \ ``file_t``\ data structure is used to describe an opened file, because in the same system in the system, the same file may be opened by multiple programs, but each opened file will uniquely execute a specific The index node, that is, only one copy of the final physical file.

Take aos\_open as an example to introduce its file opening method
-----------------------------------------------------------------

``aos_open``\ is an external interface, and external functions can directly use this interface to open files without worrying about the implementation details of the underlying file system. The code is as follows:

The input parameters are:

::

    const char *path; i.e. file path name
    int flags; namely operation flags, such as read-only, write-only, read-write, etc.

.. code:: c

    int aos_open(const char *path, int flags)
    {
        file_t *file;
        inode_t *node;
        size_t len ​​= 0;
        int ret = VFS_SUCCESS;

        if (path == NULL) {
            return -EINVAL;
        }

        len = strlen(path);
        if (len> PATH_MAX) {/* File path name is not allowed to exceed 256 bytes */
            return -ENAMETOOLONG;
        }
        /* Acquire the mutex, which is created in the vfs_init function */
        if ((ret = krhino_mutex_lock(&g_vfs_mutex, RHINO_WAIT_FOREVER)) != 0) {
            return ret;
        }
        /* Pass the parameters according to the path name, open the index node, the specific function implementation will be introduced below */
        node = inode_open(path);

        if (node ​​== NULL) {
            krhino_mutex_unlock(&g_vfs_mutex);

    #ifdef IO_NEED_TRAP
            return trap_open(path, flags);
    #else
            return -ENOENT;
    #endif
        }

        node->i_flags = flags;
        /*Because the files operated by the user are newly created files in memory (the file object will in turn point to the index node
            That is, a file may be opened by multiple programs). So you need to create a new file object based on the index contact object
        */
        file = new_file(node);
        /* Release the mutex lock */
        krhino_mutex_unlock(&g_vfs_mutex);

        if (file == NULL) {
            return -ENFILE;
        }
        /* Determine whether the path name points to a file or a directory according to the node type, because although the file object and the directory object are both nodes
        But its operation method is somewhat different, see the directory and file operation method in the previous article */
        if (INODE_IS_FS(node)) {
            if ((node->ops.i_fops->open) != NULL) {
                ret = (node->ops.i_fops->open)(file, path, flags);
            }

        } else {
            if ((node->ops.i_ops->open) != NULL) {
                ret = (node->ops.i_ops->open)(node, file);
            }
        }

        if (ret != VFS_SUCCESS) {
            del_file(file);
            return ret;
        }
        /* Get the file handle */
        return get_fd(file);
    }
 
- inode\_open The inode\_open function is used to open the corresponding node according to the file path name.
   The input parameters are: ``const char * path; file path name`` The output parameters are:
   ``inode_t; corresponding node``

.. code:: c

    static inode_t g_vfs_dev_nodes[AOS_CONFIG_VFS_DEV_NODES];
    inode_t *inode_open(const char *path)
    {
        int e = 0;
        inode_t *node;
        /*AOS_CONFIG_VFS_DEV_NODES This macro is defined as 25.
            That is, only 25 nodes will be saved in the array g_vfs_dev_nodes that saves the nodes
        */
        for (e = 0; e <AOS_CONFIG_VFS_DEV_NODES; e++) {
            node = &g_vfs_dev_nodes[e];

            if (node->i_name == NULL) {
                continue;
            }
            /* Determine whether the node is a directory or a file */
            if (INODE_IS_TYPE(node, VFS_TYPE_FS_DEV)) {
                if ((strncmp(node->i_name, path, strlen(node->i_name)) == 0) &&
                    (*(path + strlen(node->i_name)) =='/')) {
                    return node;
                }
            }
            if (strcmp(node->i_name, path) == 0) {
                return node;
            }
        }

        return NULL;
    }

- new\_file
   In the new\_file() function, the main function completed is to create a new file\_t structure definition and initialization.
   The input parameter is: inode\_t \*node; The node output parameter obtained in the previous function is:
   file\_t type. Used to obtain the file handle later

.. code:: c

    static file_t files[MAX_FILE_NUM];
    #define MAX_FILE_NUM (AOS_CONFIG_VFS_DEV_NODES * 2)
    file_t *new_file(inode_t *node)
    {
        file_t *f;
        int idx;
        /* Create a new data item in the file array. And ensure that the array is not full. That is, the number of open files is limited */
        for (idx = 0; idx <MAX_FILE_NUM; idx++) {
            f = &files[idx];

            if (f->node == NULL) {
                goto got_file;
            }
        }

        return NULL;

    got_file:
        f->node = node;
        f->f_arg = NULL;
        f->offset = 0;
        inode_ref(node);
        return f;
    }

All system call functions (similar to aos\_open) are located in the vfs.c file.

Load the driver file or file system into the VFS
------------------------------------------------

Functions defined in the vfs\_register.c file:

.. code:: c

    int aos_register_driver(const char *path, file_ops_t *ops, void *arg)
    int aos_register_fs(const char *path, fs_ops_t *ops, void *arg)

The above two functions are functions to load the driver file or the file system type into the VFS respectively. External programs (such as sensor driver) can call these two interfaces to load the driver file into the VFS.

Take aos\_register\_driver as an example to introduce:

The input parameters are: Drive file path name const char \* path (/dev/null)

Drive operation method file\_ops\_t \*ops
(It is not necessary to implement all the methods, implement the necessary methods, and set the rest to NULL)

.. code:: c

    int aos_register_driver(const char *path, file_ops_t *ops, void *arg)
    {
        inode_t *node = NULL;
        int err, ret;

        err = krhino_mutex_lock(&g_vfs_mutex, RHINO_WAIT_FOREVER);
        if (err != 0) {
            return err;
        }
    //Find an empty array item in the g_vfs_dev_nodes array, return its pointer to node, and assign the path name of path to node-->name
        ret = inode_reserve(path, &node);
        if (ret == VFS_SUCCESS) {
            /* now populate it with char specific information */
            INODE_SET_CHAR(node);

            node->ops.i_ops = ops;
            node->i_arg = arg;
        }

        /* step out critical area for type is allocated */
        err = krhino_mutex_unlock(&g_vfs_mutex);
        if (err != 0) {
            if (node->i_name != NULL) {
                krhino_mm_free(node->i_name);
            }

            memset(node, 0, sizeof(inode_t));
            return err;
        }

        return ret;
    }

Sample code
-----------

The operation of vfs is operated in linux,
Here is an example \ ``aos_open``\, \ ``aos_close``\, \ ``aos_read``\, \ ``aos_write``

.. code:: c

    void bl_test_uart0(void)
    {
        int fd;
        int length;
        char buf_recv[128];

        /* First open the relevant file, corresponding to UART0 */
        fd = aos_open("/dev/ttyS0", 0);
        if (fd <0) {
            log_error("open err.\r\n");
            return;
        }

        while (1) {
            /* Read the data in UART0 */
            length = aos_read(fd, buf_recv, sizeof(buf_recv));
            if (length> 0) {

                log_info("recv len = %d\r\n", length);

                /* Until the receipt of'exit' will actively end the loop and close related files */
                if (memcmp(buf_recv, "exit", 5) == 0) {
                    aos_close(fd);
                    break;
                }

                /* UART0 will return the received data */
                aos_write(fd, buf_recv, length);
            }
            vTaskDelay(100);
        }
    }

Notes
-----

- An important mutex lock of VFS All operations related to VFS need to acquire the mutex lock to proceed.
   ``kmutex_t g_vfs_mutex;``

- The two important array structures of VFS are as follows: The first array is an array structure for storing nodes.
   The second array is an array structure that holds file objects. Directly related to the user is the second array structure

.. code:: c

    static inode_t g_vfs_dev_nodes[AOS_CONFIG_VFS_DEV_NODES];
    static file_t files[MAX_FILE_NUM];

- The user only needs to care about the file vfs\_register.c file is used to register vfs.c
   Files are used for various standard operations.
