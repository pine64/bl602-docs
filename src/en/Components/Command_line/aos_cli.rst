cli
===

Overview
--------

There are powerful shell tools under Linux that allow users to interact with the system. However, in traditional Embedded systems, users have to implement a set of similar interactive tools themselves. AliOS-Things comes with a set of native command line interactive tool called cli (command-line interface). In addition to providing basic system interactive, it also supports user-defined commands. We have ported it to our system, and a lot of improvements have been made to it as well. We will introduce how to use the cli tool in following section.


Example
--------

First call ``test_cli_init()`` from within the shell, then a ``test`` command could print ``hello world.`` as following.

::

    #
    #
    # test
    hello world.
    #
    #

All the useful commands are documented at `helper <helper.html>`_

.. code:: c

    static void cmd_test_func(char *buf, int len, int argc, char **argv)
    {
        printf("hello world.\r\n");
        return;
    }

    const static struct cli_command cmds_user[] = {
        {"test", "it's test func ", cmd_test_func}
    };

    int test_cli_init(void)
    {
        return aos_cli_register_commands(cmds_user, sizeof(cmds_user)/sizeof(cmds_user[0]));
    }
