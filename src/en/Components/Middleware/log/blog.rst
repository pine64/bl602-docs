blog
====

Overview
--------

Blog is an ultra-lightweight log component, very suitable for resource-sensitive software projects.

Features
--------

Blog simplifies the log into 3 categories, namely components, files, and private logs, and respectively support software dynamic modification and macro shutdown schemes (not occupying rom). Here in after, the dynamic modification is collectively referred to as a soft switch, and the macro complete shutdown scheme is a static switch.

- Component log management

This log has the highest priority. The following file logs and private logs are bound by this switch
- File log management
   In the log priority, the following private logs are restricted by this switch, and the file log is managed by the component log.
- Private log management
This log has the lowest priority and is managed by component log and file log

Log level description
---------------------

The levels are as follows, where all is the lowest, that is, all logs are output

::

    all: All logs are output, which is actually equivalent to all
    debug: debug and above
    info: info and above
    warn: warn and above
    error: error and above
    assert: assert and above
    never: All logs are not output, which is actually equivalent to assert

Instructions
------------

Include the necessary header files ``#include <blog.h>''\ Then set the component log, file log, and private log respectively.

.. code:: c

    #include <blog.h>
    BLOG_DECLARE(blog_testc2);

    void func(void)
    {
        blog_debug("blog_testc2 debug\r\n");
        blog_info("blog_testc2 info\r\n");
        blog_warn("blog_testc2 warn\r\n");
        blog_error("blog_testc2 error\r\n");
        blog_assert("blog_testc2 assert\r\n");

        blog_debug_user(blog_testc2,"blog_testc2 debug user\r\n");
        blog_info_user(blog_testc2,"blog_testc2 info user\r\n");
        blog_warn_user(blog_testc2,"blog_testc2 warn user\r\n");
        blog_error_user(blog_testc2,"blog_testc2 error user\r\n");
        blog_assert_user(blog_testc2,"blog_testc2 assert user\r\n");
    }

- Component log switch

   - Static switch in the corresponding proj\_config.mk
      Add the name of the corresponding component to the LOG\_ENABLED\_COMPONENTS configuration under the file directory
      For example, blog\_testa blog\_testb needs to be added here
      Blog\_testc component static switch, other components are closed by default
      ``LOG_ENABLED_COMPONENTS:=blog_testa blog_testb blog_testc``
   - Software switch Enable the log output level by inputting the following command, for example, logset level
      component\_name For example: ``blogset assert blog_testc``

- File log management

   - Static switch
      In the corresponding \*.c file, add this line of code. Note that whether it is on or off, you must choose one.
      ``The default is on`` ``#define BLOG_HARD_DECLARE_DISABLE 1 // Off``
   - Software switch Enable the log output level by inputting the following command, for example, logset level
      component\_name.file\_name For example:
      ``blogset info blog_testc.blog_testc2_full``

- Private log management

   - Static switch Use just add BLOG\_DECLARE(...), you don’t need to add this line directly.
      ``BLOG_DECLARE(blog_testc2); // Open, where 　"blog_testc2" is user-defined``
   - Software switch Enable the log output level by inputting the following command, for example, logset level
      component\_name.file\_name.pri\_name For example:
      ``blogset debug blog_testc.blog_testc2_full.blog_testc2``
