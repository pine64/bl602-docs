Yloop
=====

--------------------

-  `Yloop Overview`_

-  `Yloop Context`_

-  `Yloop Scheduling`_

-  `Yloop Implementation Principle`_

-  `Main API Introduction`_

-  `Sample Code`_

-  `Notes`_

Yloop Overview
--------------

Yloop is AliOS Things Asynchronous event framework. 
Yloop draws on common events loops of libuv and embedded industry, comprehensively considering the complexity, performance, footprint and implements an event scheduling mechanism suitable for MCU. 
We have ported related plugins. Its main advantage is that all processing is performed in the main task, without the need for additional creation tasks, thereby saving memory usage. 
At the same time, since all processing is performed in the main task, complex mutual exclusion operations are not required.

Yloop Context
-------------

Each Yloop instance (aos_loop_t) is bound to a specific task context. 
The context of the program entry of AliOS Things (application_start) is linked to the system's master Yloop instance, which is also called main task.
Other tasks can also create their own Yloop instances.

Yloop Scheduling
----------------

Yloop realizes the unified scheduling management of IO, timer, callback, and event:

-  ``IO``\ : The most common is Socket, but devices managed by VFS of AliOS Things are also included.
-  ``timer``\ : A common timer
-  ``callback``\ : Specific execution function
-  ``event``\ : Including system events and user defined events

When aos\_loop\_run is called, current task will stop and wait for the execution of above events.

Yloop Implementation Principle
------------------------------

Yloop uses the select interface of the protocol stack to implement the scheduling of IO and timer.
AliOS Things's own protocol stack exposes a special eventfd interface.
Yloop uses this interface to associate VFS device files with eventfd to realize the unified scheduling of events for the entire system.

Main API Introduction
---------------------

-  Register an event listener function

.. code:: c

    /**
     * Register system event filter callback.
     *
     @param[in]  type  event type interested.
     * @param[in]  cb    system event callback.
     * @param[in]  priv  private data past to cb.
     *
     * @return  the operation status, 0 is OK, others is error.
     */
    int aos_register_event_filter(uint16_t type, aos_event_cb cb, void *priv);

    /**
     * Unregister native event callback.
     *
     * @param[in]  type  event type interested.
     * @param[in]  cb    system event callback.
     * @param[in]  priv  private data past to cb.
     *
     * @return  the operation status, 0 is OK, others is error.
     */
    int aos_unregister_event_filter(uint16_t type, aos_event_cb cb, void *priv);

-  Publish an event

.. code:: c

    /**
     * Post local event.
     *
     * @param[in]  type   event type.
     * @param[in]  code   event code.
     * @param[in]  value  event value.
     *
     * @return  the operation status, 0 is OK,others is error.
     */
    int aos_post_event(uint16_t type, uint16_t code, unsigned long  value);

-  Register and cancel a poll event

.. code:: c

    /**
     * Register a poll event in main loop.
     *
     * @param[in]  fd      poll fd.
     * @param[in]  action  action to be executed.
     * @param[in]  param   private data past to action.
     *
     * @return  the operation status, 0 is OK,others is error.
     */
    int aos_poll_read_fd(int fd, aos_poll_call_t action, void *param);

    /**
     * Cancel a poll event to be executed in main loop.
     *
     * @param[in]  fd      poll fd.
     * @param[in]  action  action to be executed.
     * @param[in]  param   private data past to action.
     */
    void aos_cancel_poll_read_fd(int fd, aos_poll_call_t action, void *param);

-  Post and cancel a delayed action

.. code:: c

    /**static void adc_cb_read(int fd, void *param)
    {
        aos_post_event(EV_ADCKEY, CODE_ADCKEY_INT_TRIGGER, fd);
    }
     * Post a delayed action to be executed in main loop.
     *
     * @param[in]  ms      milliseconds to wait.
     * @param[in]  action  action to be executed.
     * @param[in]  arg     private data past to action.
     *
     * @return  the operation status, 0 is OK,others is error.
     */
    int aos_post_delayed_action(int ms, aos_call_t action, void *arg);

    /**
     * Cancel a delayed action to be executed in main loop.
     *
     * @param[in]  ms      milliseconds to wait, -1 means don't care.
     * @param[in]  action  action to be executed.
     * @param[in]  arg     private data past to action.
     */
    void aos_cancel_delayed_action(int ms, aos_call_t action, void *arg);

-  Schedule a callback

.. code:: c

    /**
     * Schedule a callback in next event loop.
     * Unlike aos_post_delayed_action,
     * this function can be called from non-aos-main-loop context.

     * @param[in]  action  action to be executed.
     * @param[in]  arg     private data past to action.
     *
     * @return  the operation status, <0 is error,others is OK.
     */
    int aos_schedule_call(aos_call_t action, void *arg);

Sample Code
-----------

Here we will introduce how to use \ `Event registration, notification, callback and cancellation process <#event registration, notification, callback and cancellation process>`__\ ,\ `Poll event registration cancellation <#Poll event registration cancellation>`__\ ,\ `Delay execution of an action <#Delay execution of an action>`__ and \ `Schedule a callback <#Schedule a callback>`__\

Event registration, notification, callback and cancellation process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    aos_register_event_filter(EV_WIFI, event_cb_wifi_event, NULL);

The user first calls the \ ``aos_register_event_filter``\ to register an event on monitoring function.
For example, first explicitly register a \ ``EV_WIFI``\ in the event listener function\ ``event_cb_wifi_event``

.. code:: c

    aos_post_event(EV_WIFI, CODE_WIFI_ON_INIT_DONE, 0);

When the event ``CODE_WIFI_ON_INIT_DONE`` occurs, the callback function is called to run.

.. code:: c

    static void event_cb_wifi_event(input_event_t *event, void *private_data)
    {
        switch (
            case CODE_WIFI_ON_INIT_DONE:
            {
                printf("[APP] [EVT] CODE_WIFI_ON_INIT_DONE %lld\r\n", aos_now_ms());
            }
            break;
            case CODE_WIFI_ON_PRE_GOT_IP:
            {
                printf("[APP] [EVT] connected %lld\r\n", aos_now_ms());
            }
            break;
            case CODE_WIFI_ON_GOT_IP:
            {
                printf("[APP] [EVT] GOT IP %lld\r\n", aos_now_ms());
            }
            break;
            default:
            {
                /*nothing*/
            }
        }
    }


``event_cb_wifi_event``\ will be called and the case\ ``CODE_WIFI_ON_INIT_DONE``\  is executed

.. code:: c

    aos_unregister_event_filter(EV_WIFI, event_cb_wifi_event, NULL);

If the user does not need to monitor the event, the user can actively call \ ``aos_unregister_event_filter``\ to cancel the monitoring


Poll event registration cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    /*uart*/
    fd_console = aos_open("/dev/ttyS0", 0);
    if (fd_console >= 0) {
        printf("Init CLI with event Driven\r\n");
        aos_cli_init(0);
        aos_poll_read_fd(fd_console, aos_cli_event_cb_read_get(), (void*)0x12345678);
        _cli_init();
    }

Take ``uart0`` as an example. The user first register a \ ``aos_poll_read_fd``\ poll event

.. code:: c

    aos_cancel_poll_read_fd(fd_console, action, (void*)0x12345678);

If the user does not need to poll the event, then user can call \ ``aos_cancel_poll_read_fd`` \ to cancel poll

Delay execution of an action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    aos_post_delayed_action(1000, app_delayed_action_print, NULL);

The user can call \ ``aos_post_delayed_action``\ to delay \ ``1s``\ the execution event

.. code:: c

    static void app_delayed_action_print(void *arg)
    {
        printf("test.\r\n");
    }

After \ ``1s``\, it will actively call \ ``app_delayed_action_print``\ function

.. code:: c

    aos_cancel_delayed_action(1000, app_delayed_action_print, NULL);

To cancel a delayed action directly, you can call \ ``aos_cancel_delayed_action``\. The first parameter is \ ``ms``\ .
When \ ``ms == -1``\, it means that there is no need to care whether the time is consistent.

Schedule a callback
~~~~~~~~~~~~~~~~~~~

.. code:: c

    aos_schedule_call(app_action_print, NULL);

The user actively calls \ ``aos_schedule_call``\ function

.. code:: c

    static app_action_print(void *arg)
    {
        printf("test\r\n");
    }

The \ ``app_action_print``\ function will be actively called in the next loop

Notes
--------

The Yloop API (include/aos/yloop.h) must be executed in the context of the task bound to the Yloop instance except for the following APIs:

-  aos\_schedule\_call
-  aos\_loop\_schedule\_call
-  aos\_loop\_schedule\_work
-  aos\_cancel\_work
-  aos\_post\_event
