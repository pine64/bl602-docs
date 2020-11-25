yloop
=====


- `Yloop Overview`

- `Yloop context`

- `Yloop scheduling`

- `Yloop implementation principle`

- `Main API Introduction`

- `Sample Code`

Yloop Overview
-------------

Yloop is AliOS Things's asynchronous event framework. Yloop borrows from libuv and common events in the embedded industry loop, considering the use of complexity, performance, and footprint, an event scheduling mechanism suitable for MCU is implemented. We ported related plugins. Its main advantage is that all processing is performed in the main task, without the need for additional creation tasks, thereby saving memory usage. At the same time, since all processing is performed in the main task, no complicated mutually exclusive operations are required.

Yloop context
--------------

Each Yloop instance (aos\_loop\_t) is bound to a specific task context, AliOS Things's program entry application\_start.
The context is bound to the main Yloop instance of the system, and this context is also called the main task. Tasks other than the main task can also create their own Yloop instances.

Yloop scheduling
----------------

Yloop implements unified scheduling management for IO, timer, callback, and event:

- ``IO``\: The most common is Socket, and it can also be a device managed by AliOS Things vfs
- ``timer``\: a common timer
- ``callback``\: specific execution function
- ``event``\: Including system events, user-defined events
After calling aos\_loop\_run, the current task will wait for the above-mentioned events to occur.

Yloop implementation principle
------------------------------

Yloop uses the select interface of the protocol stack to implement the scheduling of IO and timer. AliOS
Things's own protocol stack exposes a special eventfd interface. Yloop uses this interface to associate VFS device files with eventfd to realize the unified scheduling of events in the entire system.

Main API introduction
---------------------

- Register event listener function

.. code:: c

    /**
     * Register system event filter callback.
     * @param[in] type event type interested.
     * @param[in] cb system event callback.
     * @param[in] priv private data past to cb.
     *
     * @return the operation status, 0 is OK, others is error.
     */
    int aos_register_event_filter(uint16_t type, aos_event_cb cb, void *priv);

    /**
     * Unregister native event callback.
     *
     * @param[in] type event type interested.
     * @param[in] cb system event callback.
     * @param[in] priv private data past to cb.
     *
     * @return the operation status, 0 is OK, others is error.
     */
    int aos_unregister_event_filter(uint16_t type, aos_event_cb cb, void *priv);

-Post an event

.. code:: c

    /**
     * Post local event.
     *
     * @param[in] type event type.
     * @param[in] code event code.
     * @param[in] value event value.
     *
     * @return the operation status, 0 is OK, others is error.
     */
    int aos_post_event(uint16_t type, uint16_t code, unsigned long value);

-Register and cancel a poll event

.. code:: c

    /**
     * Register a poll event in main loop.
     *
     * @param[in] fd poll fd.
     * @param[in] action action to be executed.
     * @param[in] param private data past to action.
     *
     * @return the operation status, 0 is OK, others is error.
     */
    int aos_poll_read_fd(int fd, aos_poll_call_t action, void *param);

    /**
     * Cancel a poll event to be executed in main loop.
     *
     * @param[in] fd poll fd.
     * @param[in] action action to be executed.
     * @param[in] param private data past to action.
     */
    void aos_cancel_poll_read_fd(int fd, aos_poll_call_t action, void *param);

-Post and cancel a delayed action

.. code:: c

    /**static void adc_cb_read(int fd, void *param)
    {
        aos_post_event(EV_ADCKEY, CODE_ADCKEY_INT_TRIGGER, fd);
    }
     * Post a delayed action to be executed in main loop.
     *
     * @param[in] ms milliseconds to wait.
     * @param[in] action action to be executed.
     * @param[in] arg private data past to action.
     *
     * @return the operation status, 0 is OK, others is error.
     */
    int aos_post_delayed_action(int ms, aos_call_t action, void *arg);

    /**
     * Cancel a delayed action to be executed in main loop.
     *
     * @param[in] ms milliseconds to wait, -1 means don't care.
     * @param[in] action action to be executed.
     * @param[in] arg private data past to action.
     */
    void aos_cancel_delayed_action(int ms, aos_call_t action, void *arg);

- Schedule a callback

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

Sample code
------------

Here we will introduce:

- `Event registration, notification, callback, cancellation process`
- `Registration of poll event cancelled`
- `Delayed execution of an action`
- `Schedule a callback`

Event registration, notification, callback, cancellation process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    aos_register_event_filter(EV_WIFI, event_cb_wifi_event, NULL);

The user first calls \ ``aos_register_event_filter``\ register event monitoring function, for example, first explicitly register a \ ``EV_WIFI``\ event monitoring function\ ``event_cb_wifi_event``

.. code:: c

    aos_post_event(EV_WIFI, CODE_WIFI_ON_INIT_DONE, 0);

When there is a task calling \ ``aos_post_event``\ interface, post \ ``CODE_WIFI_ON_INIT_DONE``\ after the event

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

``event_cb_wifi_event``\ will be called and enter the case\ ``CODE_WIFI_ON_INIT_DONE``\ branch

.. code:: c

    aos_unregister_event_filter(EV_WIFI, event_cb_wifi_event, NULL);

If the user does not need event monitoring, the user can actively call \ ``aos_unregister_event_filter``\ cancel the monitoring

Registration of poll event canceled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    /*uart*/
    fd_console = aos_open("/dev/ttyS0", 0);
    if (fd_console >= 0) {
        printf("Init CLI with event Driven\r\n");
        aos_cli_init(0);
        aos_poll_read_fd(fd_console, aos_cli_event_cb_read_get(), (void*)0x12345678);
        _cli_init();
    }

Take ``uart0`` as an example, the user first registers a \ ``aos_poll_read_fd``\ poll event

.. code:: c

    aos_cancel_poll_read_fd(fd_console, action, (void*)0x12345678);

If the user does not need the poll of the event, the user can call \ ``aos_cancel_poll_read_fd`` \ cancel poll

Delay execution of an action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    aos_post_delayed_action(1000, app_delayed_action_print, NULL);

The user can call \ ``aos_post_delayed_action``\ make a delayed\ ``1s``\ execute event

.. code:: c

    static void app_delayed_action_print(void *arg)
    {
        printf("test.\r\n");
    }

After \ ``1s``\, it will actively call \ ``app_delayed_action_print``\ function

.. code:: c

    aos_cancel_delayed_action(1000, app_delayed_action_print, NULL);

When the user wants to cancel a delayed action directly, you can call \ ``aos_cancel_delayed_action``\, the first \ ``ms``\ parameter,
When \ ``ms == -1``\, it means that there is no need to care whether the time is consistent

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

Then the \``app_action_print``\ function will be actively called in the next loop

Precautions
-----------

The Yloop API (include/aos/yloop.h) must be executed in the context of the task bound to the Yloop instance except for the following APIs:

- aos\_schedule\_call
- aos\_loop\_schedule\_call
- aos\_loop\_schedule\_work
- aos\_cancel\_work
- aos\_post\_event
